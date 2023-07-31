use std::io;

fn main() {

    //打印字符
    println!("Hello, world!");
    let mut guess = String::new();
    io::stdin()
    .read_line(&mut guess)
    .expect("Error reading line");
println!("you guessed {guess}");
}
