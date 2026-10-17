from pathlib import Path
import re,json,subprocess
r=Path(__file__).parent;d=r/'dist'
data=json.loads(subprocess.check_output(['node','-e',"global.window={};require('./dist/data.js');process.stdout.write(JSON.stringify(window.portfolio))"],cwd=r))
# Use the paired artwork states, with the same layer geometry as the reference.
p=d/'index.html';s=p.read_text()
for base,active in [(12,11),(22,21),(17,16),(19,20),(24,25),(3,4),(6,5),(9,8)]:
 s=s.replace(f'<img src="assets/room/{base}.png" alt="">',f'<img class="rest-state" src="assets/room/{base}.png" alt=""><img class="active-state" src="assets/room/{active}.png" alt="">')
for i,key,label in [(12,'learning','My learning shelf'),(22,'projects','My projects'),(17,'vision','Computer vision lab'),(19,'engineering','How I build'),(24,'sound','Focus & connect')]:
 pattern=rf'<a class="object object-{i}".*?</a>'
 match=re.search(pattern,s);v=match.group(0)
 v=re.sub(r'<a ',f'<button type="button" data-room="{key}" aria-haspopup="dialog" aria-controls="room-dialog" ',v,1)
 v=re.sub(r' href="[^"]*"','',v).replace('</a>','</button>')
 v=re.sub(r'aria-label="[^"]*"',f'aria-label="{label}"',v)
 v=re.sub(r'<span>.*?</span>',f'<span>{label} ↗</span>',v)
 s=s[:match.start()]+v+s[match.end():]
# Initial board-games state is upright on the shelf; open state fans outward.
s=s.replace('class="object object-19"','class="object object-19"')
# Accessible quick links also work without hovering over artwork.
s=s.replace('<small class="art-note">','<div class="room-shortcuts"><a href="#projects">My work ↗</a><a href="assets/Prashanth-Reddy-Resume.pdf" download>My résumé ↓</a><a href="#about">About me ↗</a></div><small class="art-note">')
# Full journey beneath the about introduction.
journey='<div class="journey"><h3>My Journey</h3><div class="journey-track"><article><span class="journey-dot"></span><small>2022 – 2026</small><h4>B.Tech · Information Technology</h4><h5>IIIT Vadodara</h5><p>A foundation in application development, problem-solving, and software engineering.</p></article>'
for j in reversed(data['jobs']):journey+=f'<article><span class="journey-dot"></span><small>{j["date"]}</small><h4>{j["role"]}</h4><h5>{j["company"]}</h5><p>{j["body"]}</p></article>'
journey+='</div></div>'
s=s.replace('<a class="pill" href="assets/Prashanth-Reddy-Resume.pdf" download>',journey+'<a class="pill" href="assets/Prashanth-Reddy-Resume.pdf" download>')
# An authored layered flower with reversible bloom instead of a text glyph.
flower='<span class="flower-core"></span>'+''.join(f'<span class="petal" style="--petal:{i};--angle:{i*30}deg"></span>' for i in range(12))+'<span class="flower-stem"></span><span class="flower-leaf"></span>'
s=s.replace('<span>✿</span>',flower).replace('aria-label="Bloom the flower"','aria-label="Bloom the flower" aria-pressed="false"')
s=s.replace('<p>A little bloom for your day. Click to make it grow.</p>','<p>A little bloom for your day. Hover or tap to open it.</p>')
# Shared bottom-sheet dialog is native, keyboard-accessible and touch-friendly.
dialog='''<dialog id="room-dialog" class="room-dialog" aria-labelledby="sheet-title"><div class="sheet-handle" aria-hidden="true"></div><button class="sheet-close" aria-label="Close dialog">×</button><header><h2 id="sheet-title"></h2><p id="sheet-description"></p></header><div class="sheet-carousel"><button class="slide-prev" aria-label="Previous item">‹</button><div class="slide-track" tabindex="0" aria-label="Carousel"></div><button class="slide-next" aria-label="Next item">›</button></div><div class="sheet-dots" aria-label="Choose slide"></div><div class="sheet-extra"></div><p class="slide-status" role="status" aria-live="polite"></p></dialog>'''
s=s.replace('</main>', '</main>'+dialog)
p.write_text(s)
# SVG navigation icons replace font-dependent symbols on every page.
paths={'⌂':'<path d="m3 10 9-7 9 7v10H14v-6h-4v6H3z"/>','◷':'<circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><path d="M11 6h2v6l4 3-1 2-5-4z"/>','▣':'<path d="M5 3h14v18l-7-4-7 4z"/><path d="m9 8 3 3 3-3" fill="none" stroke="white" stroke-width="2"/>','♙':'<circle cx="12" cy="9" r="6" fill="none" stroke="currentColor" stroke-width="2"/><path d="m8 14-2 8 6-3 6 3-2-8" fill="none" stroke="currentColor" stroke-width="2"/>','☺':'<circle cx="12" cy="12" r="10"/><path d="M7 14q5 7 10 0" fill="none" stroke="white" stroke-width="2"/><circle cx="8" cy="9" r="1.5" fill="white"/><circle cx="16" cy="9" r="1.5" fill="white"/>','✉':'<rect x="2" y="4" width="20" height="16" rx="2" fill="none" stroke="currentColor" stroke-width="2"/><path d="m3 6 9 7 9-7" fill="none" stroke="currentColor" stroke-width="2"/>'}
for p in d.glob('*.html'):
 s=p.read_text()
 if p.name!='index.html':s=s.replace('href="#home"','href="index.html#home"')
 for icon,path in paths.items():s=s.replace(f'<b>{icon}</b>',f'<svg width="20" height="20" viewBox="0 0 24 24" fill="currentColor" aria-hidden="true">{path}</svg>')
 s=s.replace('</body>','<div class="cursor-label" aria-hidden="true"><i></i><span></span></div><script src="studio-interactions.js"></script></body>')
 p.write_text(s)
(d/'room-data.js').write_text('window.roomData='+json.dumps(data)+';')
p=d/'index.html';s=p.read_text().replace('<script src="studio-interactions.js">','<script src="room-data.js"></script><script src="studio-interactions.js">');p.write_text(s)
print('Enhanced interactive objects, carousel sheets, journey and motion assets.')
