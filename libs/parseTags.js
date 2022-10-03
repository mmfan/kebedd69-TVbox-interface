// import cheerio from 'https://gitcode.net/qq_32394351/dr_py/-/raw/master/libs/cheerio.min.js';

if(typeof(MY_URL)==='undefined'){
    var MY_URL; // 全局注入变量,pd函数需要
}
/**
 *  url拼接
 * @param fromPath 初始当前页面url
 * @param nowPath 相对当前页面url
 * @returns {*}
 */
export function urljoin(fromPath, nowPath) {
    fromPath = fromPath||'';
    nowPath = nowPath||'';
    return joinUrl(fromPath, nowPath);
    // try {
    //     // import Uri from './uri.min.js';
    //     // var Uri = require('./uri.min.js');
    //     // eval(request('https://cdn.bootcdn.net/ajax/libs/URI.js/1.19.11/URI.min.js'));
    //     // let new_uri = URI(nowPath, fromPath);

    //     let new_uri = Uri(nowPath, fromPath);
    //     new_uri = new_uri.toString();
    //     // console.log(new_uri);
    //     // return fromPath + nowPath
    //     return new_uri
    // }
    // catch (e) {
    //     console.log('urljoin发生错误:'+e.message);
    //     if(nowPath.startsWith('http')){
    //         return nowPath
    //     }if(nowPath.startsWith('/')){
    //         return getHome(fromPath)+nowPath
    //     }
    //     return fromPath+nowPath
    // }
}

/**
 * 重写pd方法-增加自动urljoin(没法重写,改个名继续骗)
 * @param html
 * @param parse
 * @param uri
 * @returns {*}
 */
export function pD(html,parse,uri){
    let ret = pdfh(html,parse);
    if(typeof(uri)==='undefined'||!uri){
        uri = '';
    }
    if(/(url|src|href|data-original|data-src)$/.test(parse)){
        if(/http/.test(ret)){
            ret = ret.substr(ret.indexOf('http'));
        }else{
            ret = urljoin(MY_URL,ret)
        }
    }
    // MY_URL = getItem('MY_URL',MY_URL);
    // console.log(`规则${RKEY}打印MY_URL:${MY_URL},uri:${uri}`);
    return ret
}

export var parseTags = {
    jsp:{
        pdfh:pdfh,
        pdfa:pdfa,
        pd:pD,
    },
    json:{
        pdfh(html, parse) {
        if (!parse || !parse.trim()){
            return '';
        }
        if (typeof (html) === 'string'){
            html = JSON.parse(html);
        }
        parse = parse.trim();
        if (!parse.startsWith('$.')){
            parse = '$.' + parse;
        }
        parse = parse.split('||');
        for (let ps of parse) {
            let ret = cheerio.jp(ps, html);
            if (Array.isArray(ret)){
                ret = ret[0] || '';
            } else{
                ret = ret || ''
            }
            if (ret && typeof (ret) !== 'string'){
                ret = ret.toString();
            }
            if(ret){
                return ret
            }
        }
    return '';
        },
        pdfa(html, parse) {
        if (!parse || !parse.trim()){
            return '';
        }
        if (typeof (html) === 'string'){
            html = JSON.parse(html);
        }
        parse = parse.trim()
        if (!parse.startsWith('$.')){
            parse = '$.' + parse;
        }
        let ret = cheerio.jp(parse, html);
        if (Array.isArray(ret) && Array.isArray(ret[0]) && ret.length === 1){
            return ret[0] || []
        }
        return ret || []
    },
        pd:function (html,parse){
            let ret = this.pdfh(html,parse);
            if(ret){
                return urljoin(MY_URL,ret);
            }
            return ret
        },
    },
    jq:{
        pdfh:pdfh,
        pdfa:pdfa,
        pd:pD,
    },
    getParse(p0){//非js开头的情况自动获取解析标签
        if(p0.startsWith('jsp:')){
            return this.jsp
        }else if(p0.startsWith('json:')){
            return this.json
        }else if(p0.startsWith('jq:')){
            return this.jq
        }else {
            return this.jq
        }
    }
};

export var stringify = JSON.stringify;