const tg = window.Telegram.WebApp; tg.expand();


async function api(path, body){
// SSO: подтвердим сессию один раз
if(!window._session_ok){
const s = await fetch('/api/session',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({initData:tg.initData})});
window._session_ok = s.ok;
}
const res = await fetch(path, body ? {method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(body)} : {});
return res.json();
}


async function loadPosts(){
const status = document.getElementById('status').value;
const items = await fetch('/api/posts'+(status?`?status=${status}`:''));
const list = await items.json();
const root = document.getElementById('list');
root.innerHTML = '';
for (const p of list){
const el = document.createElement('article');
el.className = 'card';
el.innerHTML = `<h3>${p.title||'Без названия'}</h3>
<p>${(p.text||'').slice(0,180)}${(p.text||'').length>180?'…':''}</p>
<div class="meta"><span>${p.status}</span> · <span>${p.planned_at||'—'}</span></div>`;
root.appendChild(el);
}
}


document.getElementById('status').onchange = loadPosts;
document.getElementById('new').onclick = async () => {
const title = prompt('Заголовок');
const text = prompt('Текст');
const planned_at = prompt('Дата/время (YYYY-MM-DDTHH:mm)') || null;
await api('/api/posts', { title, text, planned_at, status:'draft' });
loadPosts();
};


loadPosts();