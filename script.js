// let a={
//     title:"pfsd",
//     description :"full stack",
//     trainer :"name"
// }
// console.log(a['title']);
// console.log(typeof(a));
// let k= {name:'name'}
// let y=k;
// k="nagasiva";
// console.log(k);
// console.log(y);
// let course = ["pfsd", "jfsd", "marn", true, null];

// console.log(course[0]);
// console.log(course[1]);
// console.log(course[2]);
// console.log(course[3]);
// console.log(course[4]);
// 
// createCourse('jfsd');
// function createCourse(coursename)
// {
//     console.log('creating'+coursename)
// }
// createCourse('pfsd');
// exception context
// 1. memory phase - variable environment
// 2. codde - thread of environment
// createCourse('jfsd');

// console.log(m)
// function createCourse(coursename){
//     console.log('creating'+ coursename);
// }
// var m=10;
// console.log(m) 

// createCourse('pfsd');
// var a=100;
// console.log(a);
// console.log(this.a)
// console.log(window.a)
// console.log(this == window)
// 
// {
//     let z =10;
//     var o =20;
//     const v =30
//     console.log(z);
//     console.log(o);
// }

// console.log(v);
// 
// function hello(){
//     const x=10;
    
// }
// console.log(x);
// hello();
// 
// function add(a,b){
//     return a+b
// }
// function diff(a,b){
//     return a-b;
// }
// or
// let add =(a,b) =>{
//     return a+b
// };
// let diff=(a,b) => a-b;

// console.log(add(2,3));
// console.log(diff(2,3));
// 
// let a =10;
// function outer(){
//     a=100
//     function inner(){
//         console.log(a);
//     }
//     return inner;
// }
// let returnFunc = outer();
// a = 20;

// console.log(returnFunc);
// returnFunc();
// 
// function fetchData (callback){
//     setTimeout(() =>{
//         let data = 'fetch data done ';
//         callback(data,null);
//         },2000)
// }
// function handeldata(data, error){
//     if(error){
//         console.error(error)
//     }else{
//         console.log(data)
//     }
// }
// fetchData(handeldata);
// 
// function fetchData (callback){
//     setTimeout(() =>{
//         let data = 'fetch data done ';
//         callback(data,'server down');
//         },2000)
// }
// function handeldata(data, error){
//     if(error){
//         console.error(error)
//     }else{
//         console.log(data)
//     }
// }
// fetchData(handeldata);