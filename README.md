# Gold Spoon 금수저 — Premium Bilingual Website

A responsive, Korean-inspired restaurant website with original storefront, dining-room, and emblem illustrations. Contains five English pages and five separate Korean pages, with matching-page EN / KO navbar switches.

## Run locally

Node.js 18 or newer is required. No external npm dependencies are needed.

```bash
npm install
npm run dev
```

Open **http://localhost:4173**.

## Build for deployment

```bash
npm run build
```

The complete deployable website is created in `dist/`.

### Vercel

Push the entire source project (including `package.json`, `vercel.json`, `site/` and `tools/`) to GitHub, then import into Vercel. The included configuration runs `npm run build`, outputs `dist/`, and supports all separate language pages. No Vite plugin or special server required.

### Cloudflare Pages

For direct upload, upload the **contents of `dist/`** or use the provided `gold-spoon-premium-deploy.zip` file. For a Git-connected project set Build command to `npm run build` and output directory to `dist`.

## Page routes

| English | Korean |
|---|---|
| `/` | `/ko/` |
| `/menu/` | `/ko/menu/` |
| `/story/` | `/ko/story/` |
| `/order/` | `/ko/order/` |
| `/visit/` | `/ko/visit/` |

## Editing

- **Text & sections:** edit the HTML files under `site/` directly. `tools/generate_pages.py` can also regenerate pages from common bilingual text and menu data, but it overwrites the HTML files.
- **Styles:** `site/assets/css/styles.css`
- **Mobile navigation, menu filters and gallery lightbox:** `site/assets/js/site.js`
- **Images:** `site/assets/img/`
- **Restaurant phone/address/links:** present in each page HTML; edit consistently in both languages. If regenerating, change the constants in `tools/generate_pages.py`.

## Content and image notes

- The storefront, interior, and emblem illustrations are newly generated artwork inspired by the user-provided photos. They are **interpretive images**, not exact documentary photographs or proof of architectural details.
- The Korean dish illustrations are original SVG artwork.
- Menu names are a curated set of dishes identified from the Gold Spoon Yelp listing and other public restaurant directory listings, **not a verified official complete menu**. Prices are deliberately omitted; call the restaurant for current availability and prices.
- The Uber Eats button links directly to the Gold Spoon restaurant listing; all ordering and payments are handled by that platform, subject to local availability.
- Standard hours listed in restaurant directories: Mon–Thu 11:30 am–3 pm and 5 pm–11 pm, Fri–Sat 11:30 am–3 pm and 5 pm–midnight, Sunday noon–10 pm. Holiday hours may vary. Verify before publishing.
- The only photos used as source references for the styled illustrations were supplied in the conversation. Yelp guest photographs are **not embedded** without permission; the gallery links out to Yelp.

## Quality checks

`npm run build` verifies all ten pages, both-language switches and required assets. The repository is dependency-free for straightforward Vercel/Cloudflare deployments.
