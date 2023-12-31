var shrink = document.getElementById("shrink");
var content = document.getElementById("content");
var color_selector = document.getElementById("color_selector");
var bg_color_selector = document.getElementById("bg_color_selector");
var ft_color_selector = document.getElementById("ft_color_selector");
var catalog = document.getElementById("catalog");
var activated_cpt;
var command_hooks = [];
var user_scripts = new Set();
color_selector.onchange = () => {
    document.documentElement.style.setProperty('--color-content', color_selector.value);
    Cookies.set(jsonurl + "color_selector", color_selector.value);
}
bg_color_selector.onchange = () => {
    document.documentElement.style.setProperty('--color-bg', bg_color_selector.value);
    Cookies.set(jsonurl + "bg_color_selector", bg_color_selector.value);
}
ft_color_selector.onchange = () => {
    document.documentElement.style.setProperty('--color-font', ft_color_selector.value);
    Cookies.set(jsonurl + "ft_color_selector", ft_color_selector.value);
}
shrink.onclick = () => {
    if(shrink.classList.contains("hide")){
        shrink.classList.remove("hide");
        catalog.style.display = "block";
        catalog.scrollTop = activated_cpt.offsetTop - catalog.clientHeight / 2 + activated_cpt.clientHeight / 2;
    }
    else{
        shrink.classList.add("hide");
        catalog.style.display = "none";
    }
}

document.onkeydown = (event) => {
    if(activated_cpt == null) return;
    var cpt_target = null;
    if(event.key == 'ArrowRight'){
        cpt_target = activated_cpt.nextSibling;
    }
    else if(event.key == 'ArrowLeft'){
        cpt_target = activated_cpt.previousSibling;
    }
    else if(event.key == '='){
        var fsize = parseInt(getComputedStyle(document.documentElement).getPropertyValue("--font-size"));
        if(fsize >= 50)return;
        document.documentElement.style.setProperty("--font-size", (fsize + 5) + "px");
    }
    else if(event.key == '-'){
        var fsize = parseInt(getComputedStyle(document.documentElement).getPropertyValue("--font-size"));
        if(fsize <= 10)return;
        document.documentElement.style.setProperty("--font-size", (fsize - 5) + "px");
    }
    if(cpt_target != null){
        cpt_target.onclick();
    }
}

function kthnextSibling(elem, k) {
    for(var i = 0; i < k; ++i) {
        if(elem == null) break;
        elem = elem.nextSibling;
    }
    return elem;
}

async function fetchJSON(url) {
    const response = await fetch(url);
    const data = await response.json();
    return data;
}

async function fetchTXT(url) {
    const response = await fetch(url);
    const data = await response.text();
    return data;
}

function parse_pyobj(input_str){
    return __BRYTHON__.pyobj2jsobj(eval(__BRYTHON__.python_to_js(input_str, "__main__")).BOOK)
}

function getQueryString(name) {
    let reg = new RegExp("(^|&)" + name + "=([^&]*)(&|$)", "i");
    let r = window.location.search.substr(1).match(reg);
    if (r != null) {
        return decodeURIComponent(r[2]);
    };
    return null;
}

function user_scripts_loaded() {
    if(user_scripts.size > 0) return;
    var loaded = false;
    document.querySelectorAll("#catalog > div").forEach((elem) => {
        if(elem.title == Cookies.get(jsonurl)){
            elem.onclick();
            loaded = true;
        }
    });
    if(!loaded)catalog.firstChild.onclick();
};

async function readFileContent() {
    try {
        const [fileHandle] = await window.showOpenFilePicker({
            types: [
                {   description: "Json / Python(BOOK)",
                    accept: { "application/json": [".json", ".py"]}}
            ],
            excludeAcceptAllOption: true,
            multiple: false,
          }); // 弹出文件选择器并获取文件句柄
        const file = await fileHandle.getFile(); // 获取文件对象
        const fileContents = await file.text(); // 读取文件内容
        if(fileHandle.name.endsWith(".py")){
            mainfunc(parse_pyobj(fileContents));
        }
        else{
            mainfunc(JSON.parse(fileContents));
        }
    } catch (error) {
        console.error(error);
    }
}

function mainfunc(data) {
    data.forEach(elem => {
        if(Object.prototype.toString.call(elem)=="[object Object]"){
            var user_script = document.createElement(elem["tag"]);
            for(var key in elem){
                if(key=="tag")continue;
                if(key == "innerText"){
                    user_script.innerText = elem[key];
                }
                else if(key == 'innerHTML'){
                    user_script.innerHTML = elem[key];
                }
                else user_script.setAttribute(key, elem[key]);
            }
            if(user_script.innerHTML == ''){
                user_scripts.add(elem);
                user_script.onload = () => {
                    user_scripts.delete(elem);
                    user_scripts_loaded();
                };
            }
            document.body.appendChild(user_script);
        }
        else if(Object.prototype.toString.call(elem)=='[object String]'){
            command_hooks.push(elem);
        }
        else{
            var cpt = document.createElement("div")
            cpt.classList.add("cpt");
            cpt.title = elem[0];
            cpt.innerHTML = elem[0];

            var page_commands = [];
            for(var i = 2; i < elem.length; i++){
                page_commands.push(elem[i]);
            }

            cpt.onclick = () => {
                activated_cpt = cpt;
                document.querySelectorAll(".cpt").forEach(elem => elem.classList.remove('activated'))
                cpt.classList.add('activated');
                /////////////////////写内容/////////////////
                content.innerHTML = '';
                Cookies.set(jsonurl, elem[0]);
                var title = document.createElement("center");
                title.innerHTML = "<h1>" + elem[0]+ "</h1>";
                content.appendChild(title);
                elem[1].forEach(element => {
                    var para = document.createElement("p");
                    para.innerHTML = element;
                    content.appendChild(para);
                });
                var footlink = document.createElement("div");
                footlink.classList.add("footlink");
                if(activated_cpt.previousSibling != null){
                    var prev = document.createElement("div");
                    prev.appendChild(document.createTextNode("Prev"));
                    prev.classList.add("mylink");prev.classList.add("prevnext");
                    prev.onclick = activated_cpt.previousSibling.onclick;
                    footlink.appendChild(prev);
                }
                if(activated_cpt.nextSibling != null){
                    var next = document.createElement("div");
                    next.appendChild(document.createTextNode("Next"));
                    next.classList.add("mylink");next.classList.add("prevnext");
                    next.onclick = activated_cpt.nextSibling.onclick;
                    footlink.appendChild(next);
                }
                if(activated_cpt.previousSibling != null || activated_cpt.nextSibling != null){
                    content.appendChild(footlink);
                }
                ////////////////////////////////////////////
                document.body.scrollIntoView();
                catalog.scrollTop = activated_cpt.offsetTop - catalog.clientHeight / 2 + activated_cpt.clientHeight / 2;

                page_commands.forEach(cmd => eval(cmd));
                command_hooks.forEach(cmd => eval(cmd));
            }
            catalog.appendChild(cpt);
        }
    });
    user_scripts_loaded();
}

function load_color_from_cookies(){
    var tmpcolor;
    tmpcolor = Cookies.get(jsonurl + "color_selector");
    if(tmpcolor != null){
        color_selector.value = tmpcolor;
        color_selector.onchange();
    }
    tmpcolor = Cookies.get(jsonurl + "bg_color_selector");
    if(tmpcolor != null){
        bg_color_selector.value = tmpcolor;
        bg_color_selector.onchange();
    }
    tmpcolor = Cookies.get(jsonurl + "ft_color_selector");
    if(tmpcolor != null){
        ft_color_selector.value = tmpcolor;
        ft_color_selector.onchange();
    }
}

var jsonurl = getQueryString("json");
if(jsonurl != null){
    fetchJSON(jsonurl).then(mainfunc);
}
else{
    jsonurl = getQueryString("js");
    if(jsonurl != null){
        var data_script = document.createElement("script");
        data_script.setAttribute("src", jsonurl);
        document.body.appendChild(data_script);
    }
    else{
        jsonurl = getQueryString("py");
        if(jsonurl != null){
            fetchTXT(jsonurl).then((py_str => {
                mainfunc(parse_pyobj(py_str));
            }));
        }
        else{
            shrink.hidden = true;
            var file_selector = document.createElement("input")
            file_selector.setAttribute("type", "file");
            content.appendChild(file_selector);
            var pond = FilePond.create(file_selector, {credits: false});
            pond.on('addfile', (error, file) => {
                if (error) {
                    alert("Failed !")
                }
                jsonurl = file.file.name;
                file.file.text().then(text => {
                    if(file.file.type == "application/json"){
                        mainfunc(JSON.parse(text));
                    }
                    else if(file.file.type == "text/javascript"){
                        eval(text);
                    }
                    else{
                        mainfunc(parse_pyobj(text));
                    }
                    shrink.hidden = false;
                    if(jsonurl)load_color_from_cookies();
                })
            });
        }
    }
};
shrink.onclick();
if(jsonurl)load_color_from_cookies();