// package main

// import "fmt"

// func main() {
// 	var a string = "hi from ajith "
// 	fmt.Println(a)

// 	var b, c int = 10, 12
// 	fmt.Println(b + c)

// 	m := 12
// 	n := 10
// 	s := "addition"
// 	fmt.Println(m+n, s)
// }

//decale the value to var after asign to the code
// package main

// import "fmt"

// func main() {
// 	var a string
// 	var b int
// 	var c float32
// 	var d bool

// 	a = "ajith"
// 	b = 27
// 	c = 2.7
// 	d = true

// 	fmt.Println(a, b, c, d)
// }

// package main

// import "fmt"

// var a int = 27
// var b string

// func main() {
// 	c := 28
// 	b = "ajith bday "

// 	fmt.Println(a, b, c)

// }

// package main

// import "fmt"

// func main() {main

// 	var q, w, e, r int = 1, 2, 3, 4
// 	fmt.Println(q, w, e, r)

//		var a, v = 27, "ajith"
//		fmt.Println(a, v)
//	}
// package main

// import "fmt"

// func main() {
// 	var a int = 27
// 	var b string = "ajith"

//		fmt.Printf("the number is : %v .", a)
//		fmt.Printf("the name is : %v . and %t", b, b)
//	}
// package main

// import "fmt"

// func main() {
// 	fmt.Println("enter the number A :")
// 	var A string
// 	fmt.Scanln(&A)
// // 	fmt.Println("name is " + A + " " + "RIGHT")

// // }
// package main

// import "fmt"

// func main() {
// 	var a int = 12
// 	var b int = 12

// 	fmt.Printf("addition of the two number is %d ", a+b)
// }

/*package main

import "fmt"

func main() {
	a := 12.5
	b := 12.5

	fmt.Printf("the answer is : %f", a+b)
}  */

// package main

// import "fmt"

// func main() {
// 	p := 25
// 	q := 20
// 	q = p
// 	q -= p
// 	fmt.Print(q)

// }
/*
package main

import "fmt"

func main() {
	a := 27
	b := &a
	fmt.Print(*b)
}
*/
/*
package main

import "fmt"

func main() {

	fmt.Println("enter the number :")
	var n int
	fmt.Scanln(&n)

	if n < 27 {
		fmt.Println("its below 27")
	} else {
		fmt.Println("its above 27")
	}
}
*/
/*
package main

import "fmt"

func main() {
	var a int = 100
//IF STATEMENT
	if a > 0 {
		if a == 100 {
			//simple for loop inside the if condition
			for i := 0; i < 4; i++ {
				fmt.Println("success")
			}

		}
	}
}
*/

// package main

// import "fmt"
// // for loop use as the infinite loop
//
//	func main() {
//		for {
//			fmt.Print()
//		}
//	}
//package main

//import "fmt"

/*
func main() {
	for i := 0; i < 10; {
		i += 3
		fmt.Println(i)
	}

}
*/

// func main() {
// 	var i int = 0
// 	for i < 20 {
// 		i += 2
// 		fmt.Println(i)
// 	}

// }
// package main

// import "fmt"

//	func main() {
//		v := []string{"ajith", "kumar", "nickwin", "bhai"}
//		for i, j := range v {
//			fmt.Println(i, j)
//		}
//	}
// package main

// import "fmt"

//	func main() {
//		i := 20
//		for i := range i + 1 {
//			fmt.Println(i)
//		}
// //	}
// package main

// import "fmt"

//	func main() {
//		var day int = 4
//		switch {
//		case day == 1:
//			fmt.Print("monday")
//		case day == 2:
//			fmt.Print("tue")
//		case day == 4:
//			fmt.Print("thiii")
// //		}
// //	}
// package main

// import "fmt"

// func add(a, b int) int {
// 	return a + b
// }

// func main() {
// 	var x int
// 	var y int
// 	fmt.Print("enter the number ")
// 	fmt.Scanln(x)
// 	fmt.Print("enter the number ")
// 	fmt.Scanln(y)
// 	result := add(x, y)
// 	fmt.Println(result)
// }

// package main

// import "fmt"

// func add(x, c int) int {
// 	return x + c
// }

//	func main() {
//		result := add(1, 1)
//		fmt.Print(result)
//	}
// package main

// import "fmt"

// func conat(a string, b string) string {
// 	return a + b
// }

// func main() {
// 	x := "ajith"
// 	v := "kumar "
// 	p := conat(x, v)
// 	fmt.Print(p)
// }

// package main

// import "fmt"

// func main() {
// 	resutlt := sum(1, 2, 3, 4, 5, 6, 7)
// 	fmt.Println(resutlt)

// }

// func sum(z ...int) int {
// 	s := 0
// 	for z := range z {
// 		s += z
// 	}
// 	return s
// }

// func great

// package main

// import "fmt"

// func main() {
// 	//result := sum(1, 2, 3, 4, 5)

// 	//fmt.Println("answer: ", result)
// 	//great("ajith", 27, 2003)

// 	//assign the variable to the function
// 	newfunction := func() {
// 		fmt.Println("hallo")
// 	}
// 	newfunction()
// }

// func sum(num ...int) int {
// 	total := 0
// 	for _, n := range num {
// 		total += n
// 	}
// 	return total
// }

// // Function with a regular parameter and a variadic parameter

// func great(a string, n ...int) {
// 	fmt.Println(a)
// 	for _, ns := range n {
// 		fmt.Println(ns)
// 	}
// }

//passing agrument
// package main

// import "fmt"

// func main() {
// 	func(n string) {
// 		fmt.Print(n)

// 	}("this is agrument")
// }
// passing as agrumnet

// package main

// import (
// 	"fmt"
// )

// func gfg(i func(a, b string) string) {
// 	fmt.Println(i("ajith", "kumar"))
// }

// func main() {
// 	value := func(a, b string) string {
// 		return a + b + "s"
// 	}
// 	gfg(value)
// }

// package main

// import "fmt"

// func main() {
// 	a := func(i int) {
// 		fmt.Println("hi ajith", i)

// 	}
// 	a(27)
// }

//	func ak(a func(i int) int) {
//		a(10)
//	}
// package main

// import "fmt"

// func init() {
// 	fmt.Print("hi")
// }

// func main() {
// 	fmt.Print("hii")
// }
/*
package main

import "fmt"

func main() {
	r := mul(2, 2)
	fmt.Print(r)

}

func mul(n, m int) int {
	return n * m //, n / m
}
*/

// package main

// import (
// 	"fmt"
// 	"go/printer"
// )

// func main{
// 	fmt.Println("hi")
// }

package main

import "fmt"

func main() {
	fmt.Println("hallo")
}
