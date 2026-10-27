import { cp, mkdir, rm, readdir, readFile, stat } from 'node:fs/promises';
import { resolve, join } from 'node:path';

const project = resolve(import.meta.dirname, '..');
const source = join(project, 'site');
const target = join(project, 'dist');
const requiredPages = [
  'index.html', 'menu/index.html', 'story/index.html', 'order/index.html', 'visit/index.html',
  'ko/index.html', 'ko/menu/index.html', 'ko/story/index.html', 'ko/order/index.html', 'ko/visit/index.html'
];

await rm(target, { recursive: true, force: true });
await mkdir(target, { recursive: true });
await cp(source, target, { recursive: true });
const files = await readdir(target, { recursive: true });
for (const page of requiredPages) {
  const body = await readFile(join(target, page), 'utf8');
  if (!body.includes('class="site-header"') || !body.includes('class="lang-switch"')) {
    throw new Error(`Invalid page or missing language switch: ${page}`);
  }
}
for (const asset of ['assets/css/styles.css','assets/js/site.js','assets/img/storefront.webp','assets/img/interior.webp','assets/img/gold-spoon-emblem.webp']) {
  const entry = await stat(join(target, asset));
  if (!entry.isFile()) throw new Error(`Missing asset: ${asset}`);
}
console.log(`Gold Spoon build passed: ${requiredPages.length} routes and ${files.length} output entries in dist/`);
