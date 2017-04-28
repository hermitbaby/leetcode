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

## Consistent Hashing

normal hashing: % node, when add/delete node, data move.

* ring
* virtual node

## External sorting

* external merge sort, 多路归并；
* 归并排序，与`桶排序`之间，存在数学上的某种对偶性；

## Hashing

冲突解决策略: 

* open hashing (也称 separate chainning)
* closed hashing (也称 open addressing，办法有linear probing，二次probing)

## Calculate percentile

* 最近序数方法（The Nearest Rank method）
* 在最近序数间线性插值的方法（The Linear Interpolation Between Closest Ranks method）
  * C = 1/2
  * C = 1
  * C = 0
  
## Reverse linkedlist

三部曲：

* 保存。如果不保存下一个节点，翻转方向后，链表就断开了。
* 翻转。
* 移指针。先后次序有讲究，先移pre，再移cur；如果先移cur，链表又断开了，pre不知道往哪移动了。
  
## Add two linkedlists

两个单链表，生成相加链表：

* 转换成整数，相加完，再生成链表表示方法；问题是，链表可以很长，整数会溢出；
* My: 转换成字符串，用字符串的每个位运算，最后转换成链表；
* 用栈保存，弹栈则是从末位开始运算；需要栈空间；
* 两个链表逆序，直接生成结果链表；

## Two linkedlists intersection

两个单链表相交的一些列问题：（一个有环，一个无环链表，不可能相交）


1. 如何判断一个链表有环？如果有，返回第一个入环节点；
	
	* 快慢指针，是否相遇；如果相遇，快指针回到头节点，与慢指针再一起同速走，相遇点就是第一相交点。

2. 如何判断两个无环链表，是否相交？相交则返回第一个节点；
	
	* 无环链表相交，尾部部分一定是相同的，因为不存在一个节点指向两个不同的后继节点；
	* 第一次走的时候，并统计链表长度；
	* 长链表先走 |len1-len2| 这么多步；然后两个链表一起走，第一个相同节点即是。
	
3. 如何判断两个有环链表，是否相交？相交返回第一个相交节点；

	* 进环前相交，进环后相交，不想交；三种不同的拓扑结构
	
## Breadth first search

```
levelorder(root)
  q ← empty queue
  q.enqueue(root)
  while (not q.isEmpty())
    node ← q.dequeue()
    visit(node)
    if (node.left ≠ null)
      q.enqueue(node.left)
    if (node.right ≠ null)
      q.enqueue(node.right)
```
 
## 一个组合数公式

Cn,k = Cn-1,k + Cn-1, k-1








