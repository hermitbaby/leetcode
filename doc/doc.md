## 2sum, 3sum, 3sum closest, 4sum

<https://www.hrwhisper.me/leetcode-2-sum-3-sum-4-sum-3-sum-closest-k-sum/>

1. 2sum: 
	* 朴素解法，枚举第一、第二个数；
	* 排序，双指针收尾检查；
	* 直接hash法，值作为key
	
1. 3sum: O(n^2)
	* 排序，枚举第一个数，然后首位检查两个数的和；过程中注意去重；因为已经排序，重复的数，只会出现在相邻idx之间；
		
1. 3sum closest:
	* 与3sum基本一样，只是每次记录较小的diff
	
1. 4sum: O(n^3)
	* 与3sum套路一样，枚举第一、第二个数，双指针检查第三、第四个数；

## Letter Combinations of a Phone Number

DFS本质其实是构建了一棵树；

```
  			      ""
		  /	      |        \
		 a        b         c
      / | \     / | \     / | \
    d   e  f   d  e  f   d  e  f 
  / | \
 g  h i
	
```   

## Subset

idx 控制下一层递归的起始index

```
  			      []
		  /	      |        \
		1         2         3
      /  \       |        
    1,2  1,3     2,3     
   | 
  1,2,3
	
``` 
With duplicated elements: check whether already in result before adding

## Combinations

和`Subset`异曲同工之妙：下层递归的`start`，由本次循环中的起始`index`决定。

## Permutation

下一层递归的遍历值为`rest = rest[:idx] + rest[idx+1:]`, 即rest中去除当前值的新list





