# Prashanth Reddy — Interactive Portfolio

Complete portable version: 12 pages, interactive layered studio, hover states, carousel dialogs, skill filters, career timeline, resume download, motion controls and contact links.

## Run on your Windows PC

1. Extract the ZIP fully.
2. Install Node.js LTS from https://nodejs.org if needed.
3. Double-click `START-WINDOWS.bat`, or open this folder in VS Code and run:

```sh
npm start
```

4. Open http://localhost:3000. Keep the terminal open; press Ctrl+C to stop.

No npm dependencies: `npm install` is not required. `npm run build` validates the ready-to-deploy files in `dist`. If port 3000 is busy, use `set PORT=3001` in Windows Command Prompt before `npm start`, then open http://localhost:3001.

## Create your GitHub repository

Create an empty repository named `prashanth-portfolio` at https://github.com/new (without a README), then run from this folder:

```sh
git init -b main
git add .
git commit -m "Add interactive developer portfolio"
git remote add origin https://github.com/YOUR_USERNAME/prashanth-portfolio.git
git push -u origin main
```

Replace YOUR_USERNAME with your GitHub username. Sign in when Git requests it. If author identity is missing, configure your own Git name/email. No credentials or existing Git history are included.

## Deploy to Vercel

1. Push the folder to GitHub as above.
2. Sign in at https://vercel.com/new and import your repository.
3. Root directory: repository root; framework: **Other**; build: `npm run build`; output: `dist`.
4. Click **Deploy**.

The included `vercel.json` configures those settings. No API keys, database or environment variables are required. Subsequent pushes to the connected branch can redeploy automatically.

Alternatively, from this folder on your PC:

```sh
npx vercel login
npx vercel --prod
```

Select your own account/team and project. This requires your account authentication. Included configuration does not mean the Vercel deployment already exists.

## Edit the portfolio

- `dist/*.html`: ready-to-run editable pages.
- `dist/studio.css`: layout and animations.
- `dist/studio.js`, `dist/studio-interactions.js`: interactions.
- `dist/room-data.js`: current carousel data.
- `dist/data.js`: personal/project data used by the optional generator.
- `dist/assets/Prashanth-Reddy-Resume.pdf`: resume.
- `dist/assets/room/`: local artwork layers.
- `build_studio.py`, `enhance_studio.py`: optional generators. With Python 3 and Node installed, run `python build_studio.py` after editing the templates or `dist/data.js`. This overwrites generated HTML and room-data.js, so keep page changes in the templates when using this workflow.

## Notes

This export is static HTML/CSS/JavaScript, not React. Email actions open an email application; no server-side form or message sending is included. Sound only plays on request. Project visuals are illustrative concepts, not screenshots. Project-specific repositories were not provided, so the site links to your GitHub profile.

All artwork and the resume are local. Google Fonts is an external style resource, with system-font fallback offline. The local server binds only to your PC; use Vercel for production hosting.

Reference room artwork came from the user-requested https://www.devanshuchauhan.in/ portfolio. The character is reference artwork, not Prashanth's likeness. The export does not grant ownership or a redistribution license to third-party assets. Source URLs are in ASSET-SOURCES.md.
