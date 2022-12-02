package main

import "fmt"

type node struct {
	data int
	next *node
}
type que struct {
	head *node
	tail *node
}

func (q *que) addlast(e int) {
	new := &node{e, nil}
	if q.head == nil {
		q.head = new
		q.tail = new
	} else {
		q.tail.next = new
		q.tail = new

	}

}
func (q *que) removefirst() {
	if q.head == nil {
		fmt.Print("its empty")
		return
	} else {
		q.head = q.head.next
	}

}
func (q *que) addfirst(e int) {
	new := &node{e, nil}
	if q.head == nil {
		q.head = new
		q.tail = new
	} else {
		new.next = q.head
		q.head = new
	}

}

// func (q *que) removelast() {
// 	if q.head == nil {
// 		fmt.Print("its empty")
// 		return
// 	}
// 	p := q.head
// 	i := 0
// 	for p != nil {
// 		p = p.next
// 		i++
// 	}
// 	q.tail = p
// 	p = p.next
// 	q.tail.next = nil

// }
func (q *que) display() {
	p := q.head
	for p != nil {
		fmt.Print(p.data, "-->")
		p = p.next
	}

}

func main() {
	d := que{}
	d.addlast(10)
	d.addlast(20)
	d.addlast(30)
	d.display()
	fmt.Println()
	d.removefirst()
	d.display()
	fmt.Println()
	d.addfirst(40)
	d.display()
	// d.removelast()
	// d.display()

}
