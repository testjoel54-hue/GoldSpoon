import { createServer } from 'node:http';
import { readFile, stat } from 'node:fs/promises';
import { resolve, join, sep, extname } from 'node:path';

const name = process.argv[2] || 'site';
const root = resolve(import.meta.dirname, '..', name);
const port = Number(process.env.PORT || 4173);
const mime = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'application/javascript; charset=utf-8','.svg':'image/svg+xml','.webp':'image/webp','.png':'image/png','.ico':'image/x-icon','.txt':'text/plain; charset=utf-8'};
createServer(async(req,res)=>{
  try {
    let urlPath = decodeURIComponent(new URL(req.url,'http://localhost').pathname);
    if(urlPath.includes('\0')) throw new Error('Invalid path');
    const filePath=resolve(root,'.'+urlPath);
    if(filePath!==root && !filePath.startsWith(root+sep)){
      res.writeHead(403);return res.end('Forbidden');
    }
    let destination=filePath;
    let details=await stat(destination).catch(()=>null);
    if(details?.isDirectory()){
      if(!urlPath.endsWith('/')){
        res.writeHead(308,{Location:urlPath+'/'});return res.end();
      }
      destination=join(destination,'index.html');
      details=await stat(destination).catch(()=>null);
    }
    if(!details?.isFile()){
      res.writeHead(404,{'Content-Type':'text/plain; charset=utf-8'});return res.end('Not found');
    }
    const body=await readFile(destination);
    res.writeHead(200,{'Content-Type':mime[extname(destination)]||'application/octet-stream','Cache-Control':'no-cache'});
    res.end(body);
  } catch(e){res.writeHead(500);res.end('Server error');console.error(e.message)}
}).listen(port,'0.0.0.0',()=>console.log(`Serving ${name} at http://localhost:${port}`));
