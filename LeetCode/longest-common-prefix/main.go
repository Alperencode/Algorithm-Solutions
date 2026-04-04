// 14. Longest Common Prefix
// https://leetcode.com/problems/longest-common-prefix
package main

func longestCommonPrefix(strs []string) string {
	if len(strs) < 1 {
		return ""
	}

	longest_prefix := strs[0]
	for i := range len(strs) {
		temp_prefix := ""
		word := strs[i]

		rang := min(len(word), len(longest_prefix))
		for j := range rang {
			if word[j] != longest_prefix[j] {
				break
			}
			temp_prefix += string(word[j])
		}

		longest_prefix = temp_prefix
	}

	return longest_prefix
}
