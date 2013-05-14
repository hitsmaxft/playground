package main

type MyIntf interface {
    Show() int
}

type MyStr struct {
    Name string
}

func (self *MyStr) Show () int{
    print(self.Name + "\n")
    return 0
}
func main(){
    ms := MyStr{"tom"}
    //ms.Name="tom"
    var it MyIntf = ms
    ms.Show()
    it.Show()
}
