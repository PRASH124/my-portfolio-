import fs from 'node:fs';import path from 'node:path';import {fileURLToPath} from 'node:url';import {execFileSync} from 'node:child_process';
const root=fileURLToPath(new URL('../',import.meta.url)),dist=path.join(root,'dist');let count=0;
for(const name of fs.readdirSync(dist)){if(name.endsWith('.html')){const html=fs.readFileSync(path.join(dist,name),'utf8');for(const match of html.matchAll(/(?:src|href)="([^"]+)"/g)){const value=match[1];if(/^(?:https?:|mailto:|data:|#)/.test(value))continue;const dest=value.split(/[?#]/)[0];if(!fs.existsSync(path.join(dist,dest)))throw new Error(`${name}: missing ${dest}`)}count++}if(name.endsWith('.js'))execFileSync(process.execPath,['--check',path.join(dist,name)])}
for(const n of [0,1,3,4,5,6,8,9,11,12,14,16,17,19,20,21,22,24,25])if(!fs.existsSync(path.join(dist,`assets/room/${n}.png`)))throw new Error('Missing room artwork '+n);
if(!fs.readFileSync(path.join(dist,'assets/Prashanth-Reddy-Resume.pdf')).subarray(0,4).equals(Buffer.from('%PDF')))throw new Error('Resume PDF is invalid');
console.log(`Validated ${count} pages, JavaScript, room assets and resume. No compilation needed.`);
