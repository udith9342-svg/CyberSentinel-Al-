const form=document.querySelector('#scan-form');
const kind=document.querySelector('#kind');
const sample=document.querySelector('#sample');
const uploadWrap=document.querySelector('#upload-wrap');
const fileInput=document.querySelector('#file');
const output=document.querySelector('#output');
const button=document.querySelector('#analyze');
function syncInputMode(){const media=['audio','video'].includes(kind.value);uploadWrap.hidden=!media;sample.placeholder=kind.value==='url'?'Paste the full URL here...':kind.value==='email'?'Paste the email subject and body here...':kind.value==='message'?'Paste the suspicious message here...':'Add optional context, then attach a file...';}
kind.addEventListener('change',syncInputMode);
form.addEventListener('submit',async event=>{
 event.preventDefault();
 const file=fileInput.files[0];
 const text=sample.value.trim();
 if(!text&&!file){show('Input required','Paste content or attach an audio/video file.');return;}
 if(['audio','video'].includes(kind.value)&&!file){show('File required','Choose an audio or video file for this analysis.');return;}
 if(file&&file.size>20*1024*1024){show('File too large','Please choose a file smaller than 20 MB.');return;}
 const body=new FormData();body.append('input_type',kind.value);body.append('text',text);if(file)body.append('file',file);
 button.disabled=true;button.firstChild.textContent='Analyzing...';show('Processing','Connecting to the CyberSentinel backend...');
 try{
  const response=await fetch('http://127.0.0.1:8000/analyze',{method:'POST',body});
  const data=await response.json();if(!response.ok)throw new Error(data.detail||'The backend returned an error.');
  render(data);
 }catch(error){show('Backend connection failed',error.message+' Start the FastAPI server and try again.');}
 finally{button.disabled=false;button.firstChild.textContent='Analyze sample ';}
});
function show(title,message){output.hidden=false;output.replaceChildren();const h=document.createElement('h3');h.textContent=title;const p=document.createElement('p');p.textContent=message;output.append(h,p);}
function render(data){output.hidden=false;output.replaceChildren();const h=document.createElement('h3');h.textContent=data.risk_level||data.status||'Analysis response';const p=document.createElement('p');p.textContent=data.summary||data.message||'No summary returned.';output.append(h,p);if(data.findings?.length){const ul=document.createElement('ul');data.findings.forEach(item=>{const li=document.createElement('li');li.textContent=item;ul.append(li);});output.append(ul);}if(data.recommendation){const rec=document.createElement('p');rec.textContent=data.recommendation;output.append(rec);}}
syncInputMode();