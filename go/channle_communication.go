package main
var str string

//no triggerd goroutine
func test_case_1() {
    go func () { str="hello" }()
    print(str)
}

var chn = make(chan int, 10)

//triggerd goroutine with sendding channel message
func test_case_2(){
    //closure
    backendforchan := func () {
        str ="hello world"
        chn <-0
    }

    go backendforchan()
    //send message
    <-chn
    print(str)
}

func main(){
    print(":call backend\n");
    test_case_1()
    print(":call backend2\n");
    test_case_2()
}
