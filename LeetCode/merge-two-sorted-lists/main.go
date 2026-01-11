// 21. Merge Two sorted
// https://leetcode.com/problems/merge-two-sorted-lists
package main

type ListNode struct {
	Val  int
	Next *ListNode
}

func mergeTwoLists(list1 *ListNode, list2 *ListNode) *ListNode {
	var merged []*ListNode

	tmp := list1
	for tmp != nil {
		merged = append(merged, tmp)
		tmp = tmp.Next
	}

	tmp = list2
	for tmp != nil {
		merged = append(merged, tmp)
		tmp = tmp.Next
	}

	for i := range len(merged) {
		for j := range len(merged[i:]) {
			if merged[i+j].Val < merged[i].Val {
				tmp := merged[i]
				merged[i] = merged[i+j]
				merged[i+j] = tmp
			}
		}
	}

	for i := range len(merged) {
		if i == len(merged)-1 {
			merged[i].Next = nil
			break
		}

		merged[i].Next = merged[i+1]
	}

	if len(merged) == 0 {
		return nil
	}
	return merged[0]
}
