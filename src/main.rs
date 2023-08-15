

fn main() {

    //打印字符
    println!("Hello, world!");

 println!("mx1jjjjd");
 // set variable
 let x = 5 ;   //is immutable variable
 println!("The variable value is ={x}");
//  x=6;   cannot assign twice to immutable variable
//  println!("The variable value is ={x}");
 
 let mut x1 = 5 ; // add "mut" and the variable is changeable ,use mut mark ,the variable must be same type
 println!("The variable value is ={x1}");
 let  x1 = 51 ; // 
 println!("The variable value is ={x1}");
 //data type
 let stringtToNum:u32= "1".parse().expect("error 1111");
 println!("{stringtToNum}");

 //tup元组
 let tup:(u32, f32) =(1,1.1);
 let tup1=tup.1;
 println!("{tup1},tup1");
// function return 
let funcmxd =mxd();
println!("the func is={funcmxd}");


}

fn mxd() -> String{
    "mxd".to_string()
}