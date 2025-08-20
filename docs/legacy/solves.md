## 2073. Time Needed to Buy Tickets
[LeetCode 2073 Link](https://leetcode.com/problems/time-needed-to-buy-tickets)

This solution efficiently simulates the ticket buying process. The time complexity is O(n*m) where n is the number of people in the queue and m is the maximum number of tickets a person wants to buy. Though not the most efficient in terms of time complexity, given the constraints, this solution works well for the input size specified.

To solve this problem, we'll simulate the process of buying tickets. We keep track of the total time taken and reduce the number of tickets for each person by one in each pass until the person at position k has bought all their tickets. Here's the strategy:

- Initialize a time counter to 0.
- Iterate over the tickets array, reducing the ticket count for each person by one in each iteration (signifying the purchase of a ticket) and incrementing the time counter.
- After each person buys a ticket, check if the person at position k has finished buying their tickets. If so, break out of the loop.
- If a person's ticket count reaches zero, they leave the queue, but since we are iterating over the original array without modifying its structure, we treat it as if the person with zero tickets does not affect the loop anymore (their ticket count cannot go below zero).

> The time complexity is O(n*m) where n is the number of people in the queue and m is the maximum number of tickets a person wants to buy.
> 
Here's how the code looks with these steps:

### Python
```python
class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        time = 0  # Initialize the counter to keep track of the time
        while tickets[k] > 0:  # Loop until the person at position k has no tickets left to buy
            for i in range(len(tickets)):  # Iterate through each person in the line
                if tickets[i] > 0:  # If the person has tickets to buy
                    tickets[i] -= 1  # Buy a ticket
                    time += 1  # Increment the time
                if tickets[k] == 0:  # If the person at position k has bought all their tickets
                    return time  # Return the total time taken
        return time  # Just in case, but this line should never be reached as the function returns in the loop
```

### JavaScript
```javascript
/**
 * Calculates the time required for the k-th person to buy all their tickets.
 * @param {number[]} tickets - Array representing the number of tickets each person wants to buy.
 * @param {number} k - The index of the person in the queue.
 * @return {number} - The total time taken for the k-th person to buy all their tickets.
 */
var timeRequiredToBuy = function(tickets, k) {
    let time = 0; // Init time counter. Every tick is a ticket buy.
    while (tickets[k] > 0) { // Loop till k-th person's tickets are bought.
        for (let i = 0; i < tickets.length; i++) { // Simulate the queue movement.
            if (tickets[i] > 0) { // If person i has tickets to buy...
                tickets[i] -= 1; // ...they buy one.
                time += 1; // Increment the time for each ticket bought.
                if (tickets[k] === 0) return time; // If k-th person's done, exit early.
            }
        }
    }
    return time; // Safety net, but the logic ensures we exit in the loop.
};
```

### Java
```java
class Solution {
    /**
     * Simulates the process of buying tickets in a queue to determine the time it takes for the k-th person to buy all theirs.
     * @param tickets Array representing the number of tickets each person in the queue wants to buy.
     * @param k The index of the person whose total time to buy tickets we're calculating.
     * @return The total time taken for the person at index k to buy all their tickets.
     */
    public int timeRequiredToBuy(int[] tickets, int k) {
        int time = 0; // Init the stopwatch.
        while (tickets[k] > 0) { // Keep going till our k-th person is ticketless.
            for (int i = 0; i < tickets.length; i++) { // One loop = one sec, per person in line.
                if (tickets[i] > 0) { // If they've got tickets to buy...
                    tickets[i]--; // ...they buy one.
                    time++; // Crank the time up by one.
                    if (tickets[k] == 0) return time; // If k-th person's done, clock out early.
                }
            }
        }
        return time; // Just for formality. We exit via the loop.
    }
}
```

### C#
```C#
public class Solution {
    /**
     * Simulates buying tickets in a queue to find out how long it takes for the k-th person to buy all of theirs.
     * @param tickets Array showing how many tickets each person wants to buy.
     * @param k Index of the person we're focusing on.
     * @return Total time taken for the k-th person to buy all their tickets.
     */
    public int TimeRequiredToBuy(int[] tickets, int k) {
        int time = 0; // Kicks off the timer.
        while (tickets[k] > 0) { // Loop 'til k's tickets are all bought.
            for (int i = 0; i < tickets.Length; i++) { // March through the queue.
                if (tickets[i] > 0) { // If someone still wants to buy...
                    tickets[i]--; // They get 1 ticket.
                    time++; // And the clock ticks once.
                    if (tickets[k] == 0) return time; // If k is done, we're done.
                }
            }
        }
        return time; // Technically unreachable, but here for completeness.
    }
}
```

## 950 Reveal Cards In Increasing Order
[LeetCode Link 950](https://leetcode.com/problems/reveal-cards-in-increasing-order)

### Python
- Sort the deck array in descending order.
- Initialize an empty list to hold the final arrangement of the deck.
- Iterate through the sorted deck:
    - For each element, insert it at the beginning of the final arrangement list.
    - If the final arrangement list has more than one element, remove the last element and insert it at the beginning of the list.
- This reverse process simulates the revealing and reordering steps backward, giving the correct initial arrangement.

```python
class Solution(object):
    def deckRevealedIncreasing(self, deck):
        """
        :type deck: List[int]
        :rtype: List[int]
        """
        # Step 1: Sort the deck in descending order to simulate the process backwards
        deck.sort(reverse=True)
        
        # Step 2: Initialize the arrangement list
        arrangement = []
        
        # Step 3: Iterate through the sorted deck
        for card in deck:
            if arrangement:
                # Move the last card to the front (simulate 'put the next top card at the bottom')
                arrangement.insert(0, arrangement.pop())
            # Reveal the card by inserting it at the front
            arrangement.insert(0, card)
        
        return arrangement
```
> This code effectively reverses the process of revealing and reordering the cards, ensuring the final arrangement allows for the cards to be revealed in increasing order. By starting with the highest card and working backward, we can place each card in such a way that the revealing process will order them correctly.

### Java
For the Java version, we'll apply a similar logic as discussed previously but adjusted for Java's syntax and type system. Here's a step-by-step implementation:

- Sort the input `deck` in ascending order.
- Use a Deque (double-ended queue) to simulate the process of revealing cards and placing the next top card at the bottom of the deck.
- Iterate through the sorted `deck` in reverse order, inserting elements to the front of the queue and then moving the previously front element to the back. This effectively simulates the process in reverse.
- Convert the Deque back to an array to return the result.

```java
import java.util.Arrays;
import java.util.Deque;
import java.util.LinkedList;

class Solution {
    public int[] deckRevealedIncreasing(int[] deck) {
        // Step 1: Sort the deck in ascending order
        Arrays.sort(deck);
        
        // Step 2: Initialize the Deque to simulate the arrangement process
        Deque<Integer> deque = new LinkedList<>();
        
        // Step 3: Iterate through the deck in reverse order
        for (int i = deck.length - 1; i >= 0; --i) {
            if (!deque.isEmpty()) {
                // Move the last element to the front to simulate the reordering
                deque.addFirst(deque.removeLast());
            }
            // Insert the current card at the front of the deque
            deque.addFirst(deck[i]);
        }
        
        // Step 4: Convert the deque back to an array
        int[] result = new int[deck.length];
        for (int i = 0; i < deck.length; ++i) {
            result[i] = deque.removeFirst();
        }
        
        return result;
    }
}
```

### JavaScript

```javascript
/**
 * Reorders the deck to reveal cards in increasing order.
 * @param {number[]} deck - The deck of cards.
 * @return {number[]} - The reordered deck.
 */
var deckRevealedIncreasing = function(deck) {
    // Step 1: Sort the deck in ascending order
    deck.sort((a, b) => a - b);
    
    // Initialize an array to simulate the deck rearrangement process
    let rearranged = [];
    
    // Step 3: Iterate through the deck in reverse order
    for (let i = deck.length - 1; i >= 0; i--) {
        if (rearranged.length > 1) {
            // Move the last card to the front to simulate the reveal process backwards
            rearranged.unshift(rearranged.pop());
        }
        // Insert the current card at the front
        rearranged.unshift(deck[i]);
    }
    
    // Return the rearranged deck
    return rearranged;
};
```

### Rust
For Rust, we will implement a solution that mirrors the logic applied in other languages, adapting it to Rust's unique syntax and ownership rules. Here's how you can do it:

- Sort the deck in ascending order.
- Use a `VecDeque` to efficiently simulate the reverse process of revealing cards and placing the next top card at the bottom of the deck.
- Iterate through the sorted deck in reverse order, simulating the process in reverse by inserting elements to the front of the VecDeque and moving the previously front element to the back.
- Convert the VecDeque back into a Vec to return the result.
Here's the Rust code implementing this approach:

```rust
use std::collections::VecDeque;

impl Solution {
    pub fn deck_revealed_increasing(mut deck: Vec<i32>) -> Vec<i32> {
        // Step 1: Sort the deck in ascending order.
        deck.sort_unstable();
        
        // Step 2: Initialize the VecDeque to simulate the arrangement process.
        let mut deque: VecDeque<i32> = VecDeque::new();
        
        // Step 3: Iterate through the deck in reverse order.
        for &card in deck.iter().rev() {
            if let Some(rear) = deque.pop_back() {
                // Move the last element to the front to simulate the reordering.
                deque.push_front(rear);
            }
            // Insert the current card at the front of the deque.
            deque.push_front(card);
        }
        
        // Step 4: Convert the VecDeque back into a Vec to return.
        Vec::from(deque)
    }
}

```

### C#
This C# solution mirrors the logic previously explained:

- Sort the deck to know the final order of revealed cards.
- Use a queue to simulate revealing cards and moving the next top card to the bottom. Since the queue does not support inserting at the front directly, this simulation is done by first dequeuing an element and then enqueuing it again, effectively moving it to the bottom.
- Finally, reverse the process by filling an array from the queue in reverse order to get the initial configuration that allows revealing the cards in increasing order.

```c#
using System;
using System.Collections.Generic;

public class Solution {
    public int[] DeckRevealedIncreasing(int[] deck) {
        // Step 1: Sort the deck in ascending order
        Array.Sort(deck);
        
        // Step 2: Initialize a queue to simulate the process
        Queue<int> queue = new Queue<int>();
        
        // Step 3: Iterate through the deck in reverse order
        for (int i = deck.Length - 1; i >= 0; --i) {
            if (queue.Count > 0) {
                // Move the last element to the front to simulate the reordering
                queue.Enqueue(queue.Dequeue());
            }
            // Insert the current card at the front of the queue
            queue.Enqueue(deck[i]);
        }
        
        // Step 4: Reverse the queue to get the final arrangement
        int[] result = new int[deck.Length];
        for (int i = deck.Length - 1; i >= 0; --i) {
            result[i] = queue.Dequeue();
        }
        
        return result;
    }
}
```
## 129. Sum Root to Leaf Numbers
[Leetcode Link](https://leetcode.com/problems/sum-root-to-leaf-numbers/)

To solve this problem, the task is to compute the sum of all root-to-leaf numbers in a binary tree where each path represents a distinct number. This can be efficiently done using a Depth-First Search (DFS) approach. During the traversal, we'll maintain the current number by appending the node's value and converting the sequence to an integer on reaching a leaf node.

We can implement this using a recursive function which:

- Starts at the root and continues to traverse each node down to the leaf.
- Accumulates the number represented by the path from the root to each node.
- Adds the number to the total sum once a leaf node is reached.

Here's how the solution will look:

```python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        # Let's add some inner juice - the recursive function to compute the sums
        def dfs(node, current_number):
            if not node:
                return 0  # No node, no money.
            
            # Building the number by shifting the digits left
            current_number = current_number * 10 + node.val
            
            # Leaf node check, as only leaf nodes give us complete numbers
            if not node.left and not node.right:
                return current_number  # Full number from root to leaf
            
            # Recursively visit left and right, summing up the contributions
            return dfs(node.left, current_number) + dfs(node.right, current_number)
        
        # Let's kick off the party with the root node
        return dfs(root, 0)
```
### Explanation of the Code:

- Recursive DFS (dfs function): This function takes the current node and the number formed up to this node. For each node, it updates the number (current_number = current_number * 10 + node.val) and continues the traversal. If a leaf is reached, it returns the number formed.
- Handling of leaf nodes: Checks if a node has no children. If so, it's a leaf node, and we return the current accumulated number.
- Summing contributions: If the node is not a leaf, the function recursively calls itself for the left and right children, summing their results to get the total from all paths through the current node.

> This solution is efficient with a complexity of  O(N), where  N is the number of nodes in the tree. It effectively handles the tree traversal and number construction simultaneously without the need for additional data structures.

## 623 - Add One Row to Tree
[Leetcode 623 Link](https://leetcode.com/problems/add-one-row-to-tree/)

To solve the problem of adding a row to a binary tree at a given depth with a specific value, we need a clear understanding of tree traversal techniques. The algorithm I'll use involves a breadth-first traversal (BFS) to locate the nodes at the desired depth (depth-1). For this, we can use a queue to assist in our level-by-level traversal.

Here's how we'll implement the `addOneRow` method in the `Solution` class:

- Special Case for Root: If depth is 1, we immediately create a new root and make the existing root the left child of the new root. This step is straightforward and does not require any further traversal.
- Breadth-First Search (BFS): Use a queue to explore the tree level by level until reaching `depth-1`. For each node at this level, we'll:
  - Create new nodes with value `val`.
  - Link these new nodes to the current node's children.
  - Adjust the original child links to point to these new nodes.
- Node Replacement: Once we've located the nodes at `depth-1`, we create new nodes with the given val and adjust the pointers accordingly, ensuring the structure of the tree remains intact.

This algorithm runs efficiently given the constraints, as it processes each node in the tree at most once, resulting in a time complexity of O(n) where n is the number of nodes in the tree.

### Python

```python3
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            # New root scenario - wrap the old root
            new_root = TreeNode(val)
            new_root.left = root
            return new_root
        
        queue = [root]
        current_depth = 1
        
        # Traverse the tree to the level just before the target depth
        while current_depth < depth - 1:
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            current_depth += 1
        
        # We're now at depth-1 and can insert the new row
        for node in queue:
            old_left, old_right = node.left, node.right
            node.left = TreeNode(val)
            node.right = TreeNode(val)
            node.left.left = old_left
            node.right.right = old_right
        
        return root
```

To implement the addOneRow method in Python 2.7 within the provided codebase, we will follow a similar approach as the Python 3 version discussed earlier. This involves using a breadth-first search (BFS) to find the appropriate nodes at depth - 1 and then modify the tree by inserting new nodes with the given value val. This Python 2.7 implementation maintains the tree's structure while efficiently adding a new row, adhering closely to Python conventions and ensuring backward compatibility with the Python 2 syntax and type annotations.

Here's how you can implement this solution in Python 2.7:

```python2.7
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            # Create a new root, make the existing tree its left subtree
            new_root = TreeNode(val, left=root)
            return new_root

        queue = [root]
        current_depth = 1

        # Traverse the tree level by level until the level before the desired depth
        while current_depth < depth - 1:
            next_level = []
            for node in queue:
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)
            queue = next_level
            current_depth += 1

        # Add the new row at the specified depth
        for node in queue:
            old_left, old_right = node.left, node.right
            node.left = TreeNode(val, left=old_left)
            node.right = TreeNode(val, right=old_right)

        return root

```

### JavaScript
To implement the `addOneRow` function in JavaScript, we'll follow the same logical approach used in the Python implementation. We'll handle the special case when the depth is 1 separately, and use a breadth-first search (BFS) with a queue for inserting a new row at the specified depth.

- TreeNode Constructor: We use the TreeNode function to create new node instances. The constructor allows setting of left and right children, defaulting to null if not provided.
- Special Case for Root: If depth === 1, we create a new root and make the existing tree its left subtree.
- Breadth-First Search (BFS): Using a queue, we traverse the tree to reach the level right before the target depth. At each level, we gather the children of the nodes to continue to the next level.
- Insertion: When the desired level is reached (depth-1), for each node at this level, we:
  - Create two new nodes with the specified value val.
  - Attach the original left and right children to these new nodes.
  - Update the current nodes to point to these new nodes as their children.

Here's how the JavaScript implementation will look:

```javascript
/**
 * Adds a new row of nodes with a given value at the specified depth.
 * @param {TreeNode} root - The root of the binary tree.
 * @param {number} val - The value for the new row of nodes.
 * @param {number} depth - The depth at which to add the new row.
 * @return {TreeNode} The modified tree root.
 */
var addOneRow = function(root, val, depth) {
    if (depth === 1) {
        // New root node becomes the parent of the current tree
        let newRoot = new TreeNode(val);
        newRoot.left = root;
        return newRoot;
    }

    let queue = [root];
    let currentDepth = 1;

    // Use BFS to reach the level just before the desired depth
    while (currentDepth < depth - 1) {
        let nextLevel = [];
        for (let node of queue) {
            if (node.left) nextLevel.push(node.left);
            if (node.right) nextLevel.push(node.right);
        }
        queue = nextLevel;
        currentDepth++;
    }

    // Insert the new row of nodes
    for (let node of queue) {
        let oldLeft = node.left;
        let oldRight = node.right;
        node.left = new TreeNode(val, oldLeft, null); // New left child, keeps the old left as its child
        node.right = new TreeNode(val, null, oldRight); // New right child, keeps the old right as its child
    }

    return root;
};

```

### C++
Key Components of the Solution:
- Queue for Level-Order Traversal: We use a standard std::queue from the C++ Standard Library to perform a breadth-first search (BFS). This method ensures that we traverse the tree level by level, which is ideal for finding and manipulating nodes at a specific depth.
- Handling Special Case for depth == 1: If depth is 1, we need to add a new root to the tree. This is a straightforward case where a new root node is created, and the existing tree becomes the left child of this new root. This modification is immediate and does not require traversal of the tree.
- Traversal to depth - 1: The goal is to reach the level just before the desired depth (depth - 1). The while loop iterates until currentDepth reaches depth - 1. Inside this loop:
  - We determine the number of nodes at the current level (levelSize).
  - For each node, we check and enqueue their children (left and right) if they exist. This sets up our queue for the next level.
- Inserting the New Row: Once at the correct level (depth - 1), we iterate over the nodes at this level using the nodes stored in our queue. For each node at this level, we:
  - Store the current left and right children.
  - Create new nodes with the specified value (val) as the new left and right children.
  - Attach the stored old children to the new nodes accordingly, ensuring the subtree structure below remains intact.

```C++
#include <queue>

class Solution {
public:
    TreeNode* addOneRow(TreeNode* root, int val, int depth) {
        if (depth == 1) {
            // Create a new root and make the existing tree its left subtree
            TreeNode* newRoot = new TreeNode(val);
            newRoot->left = root;
            return newRoot;
        }

        std::queue<TreeNode*> queue;
        queue.push(root);
        int currentDepth = 1;

        // Use BFS to find the level just before the target depth
        while (currentDepth < depth - 1) {
            int levelSize = queue.size();
            for (int i = 0; i < levelSize; ++i) {
                TreeNode* node = queue.front();
                queue.pop();
                if (node->left) queue.push(node->left);
                if (node->right) queue.push(node->right);
            }
            ++currentDepth;
        }

        // At depth-1, modify the tree structure
        while (!queue.empty()) {
            TreeNode* node = queue.front();
            queue.pop();
            TreeNode* oldLeft = node->left;
            TreeNode* oldRight = node->right;
            node->left = new TreeNode(val);  // Insert new node as left child
            node->left->left = oldLeft;      // Link old left child to new node
            node->right = new TreeNode(val); // Insert new node as right child
            node->right->right = oldRight;   // Link old right child to new node
        }

        return root;
    }
};

```
## 463 - Island Perimeter
[Leetcode 463 Link](https://leetcode.com/problems/island-perimeter)

To determine the perimeter of the island in the given grid, we can iterate through each cell of the grid. For each land cell, we can calculate the perimeter by checking its adjacent cells (up, down, left, right) to see if they are water or are outside the grid boundary. The perimeter of the island is then the sum of the count of water cells adjacent to land cells.

Let's break down the logic of the islandPerimeter function:

- Initialization: Start by initializing the perimeter variable to 0. This variable will store the total perimeter of the island. Also, retrieve the number of rows (rows) and columns (cols) in the grid.
- Iterate through the grid: Use nested loops to iterate through each cell of the grid.
Check if the cell is land: For each cell in the grid, check if it represents land (i.e., the cell value is 1).
- Calculate perimeter for each land cell:
  - When encountering a land cell, add 4 to the perimeter. This is because each land cell contributes 4 units to the perimeter since it has four sides.
  - Check adjacent cells to the current land cell to determine if they are also land cells:
    - If there's a land cell to the left (grid[i][j - 1]) of the current cell, it shares a side with the current cell. In this case, subtract 2 from the perimeter because one side is shared.
    - If there's a land cell above (grid[i - 1][j]) the current cell, it also shares a side with the current cell. Subtract 2 from the perimeter for the same reason.
- Return the total perimeter: After iterating through all cells in the grid, return the calculated perimeter value, which represents the total perimeter of the island.

The algorithm effectively calculates the perimeter of the island by considering the properties of land and water cells and how they contribute to the overall perimeter.

### Python

```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    perimeter += 4
                    if i > 0 and grid[i - 1][j] == 1:
                        perimeter -= 2
                    if j > 0 and grid[i][j - 1] == 1:
                        perimeter -= 2

        return perimeter
```
> This function iterates through each cell of the grid. If the cell is land (grid[i][j] == 1), it adds 4 to the perimeter (representing the four sides of the square). Then, it checks if there are adjacent land cells (up and left) and subtracts 2 from the perimeter for each adjacent land cell found, as the shared side between two adjacent land cells doesn't contribute to the perimeter. Finally, it returns the total perimeter calculated.

### JavaScript

This JavaScript implementation follows the same logic as described earlier for the Python implementations. It iterates through each cell of the grid, calculates the perimeter of each land cell by adding 4 (representing the four sides of the square), and subtracts 2 for each adjacent land cell found (up and left), as the shared side doesn't contribute to the perimeter. Finally, it returns the total perimeter calculated.

```javascript
/**
 * @param {number[][]} grid
 * @return {number}
 */
var islandPerimeter = function(grid) {
    let perimeter = 0;
    const rows = grid.length;
    const cols = grid[0].length;

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < cols; j++) {
            if (grid[i][j] === 1) {
                perimeter += 4;
                if (i > 0 && grid[i - 1][j] === 1) {
                    perimeter -= 2;
                }
                if (j > 0 && grid[i][j - 1] === 1) {
                    perimeter -= 2;
                }
            }
        }
    }

    return perimeter;
};
```

### C++

This implementation follows the same logic as described earlier for the Python implementation. It iterates through each cell of the grid, calculates the perimeter of each land cell by adding 4 (representing the four sides of the square), and subtracts 2 for each adjacent land cell found (up and left), as the shared side doesn't contribute to the perimeter. Finally, it returns the total perimeter calculated.

```C++
#include <vector>
using namespace std;

class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int perimeter = 0;
        int rows = grid.size();
        int cols = grid[0].size();

        for (int i = 0; i < rows; ++i) {
            for (int j = 0; j < cols; ++j) {
                if (grid[i][j] == 1) {
                    perimeter += 4;
                    if (i > 0 && grid[i - 1][j] == 1) {
                        perimeter -= 2;
                    }
                    if (j > 0 && grid[i][j - 1] == 1) {
                        perimeter -= 2;
                    }
                }
            }
        }

        return perimeter;
    }
};
```
## 1971. Find if Path Exists in Graph

[1971 LeetCode Link](https://leetcode.com/problems/find-if-path-exists-in-graph)

To solve the problem of determining if there is a valid path from a source to a destination in an undirected graph, we can utilize a graph traversal algorithm. Specifically, Breadth-First Search (BFS) is a suitable choice for this task, given its efficiency in exploring nodes layer by layer.

The approach involves:

- Constructing an adjacency list from the edges, which makes traversing the graph's connections easier.
- Using BFS to explore the graph starting from the source node and checking if we can reach the destination.

### Python

```python3
from collections import deque, defaultdict

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        # Step 1: Build the graph using adjacency list
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        # Step 2: BFS to find the path from source to destination
        queue = deque([source])
        visited = set()
        visited.add(source)
        
        while queue:
            node = queue.popleft()
            if node == destination:
                return True
            for neighbor in graph[node]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        
        # If BFS completes without finding the destination
        return False
```

> Code Debrief:
> - Adjacency List Construction: We convert the edge list into a more accessible adjacency list format, where each vertex maps to a list of connected vertices. This structure facilitates efficient traversal.
> - BFS Implementation: Using a queue, we start from the source vertex and explore each vertex's neighbors. We mark each visited vertex to prevent revisits and continue until we find the destination or exhaust the vertices.
> - Graph Traversal Logic: If during traversal we reach the destination, we return True. If the BFS completes without reaching the destination, the method returns False, indicating no valid path exists.
> This solution effectively handles large inputs up to the problem's constraints due to its O(V + E) time complexity, where V is the number of vertices and E is the number of edges.


### JavaScript

To tackle the problem of determining if there's a valid path between two nodes in an undirected graph using JavaScript, we can apply a similar approach as before but using Breadth-First Search (BFS) in JavaScript.

```javascript
/**
 * @param {number} n
 * @param {number[][]} edges
 * @param {number} source
 * @param {number} destination
 * @return {boolean}
 */
var validPath = function(n, edges, source, destination) {
    // Step 1: Construct the graph using an adjacency list
    const graph = {};
    for (let [u, v] of edges) {
        if (!graph[u]) graph[u] = [];
        if (!graph[v]) graph[v] = [];
        graph[u].push(v);
        graph[v].push(u);
    }
    
    // Step 2: Use BFS to find a path from source to destination
    const queue = [source];
    const visited = new Set();
    visited.add(source);
    
    while (queue.length > 0) {
        const node = queue.shift();
        if (node === destination) {
            return true; // Found a path
        }
        for (let neighbor of graph[node] || []) {
            if (!visited.has(neighbor)) {
                visited.add(neighbor);
                queue.push(neighbor);
            }
        }
    }
    
    // If we finish the BFS without finding the destination
    return false;
};
```

### C++
For the C++ implementation of the problem to determine if there's a valid path between two nodes in a bi-directional graph, we'll adopt a similar approach using Breadth-First Search (BFS). BFS is ideal for this scenario because it effectively searches layer by layer from the source, ensuring all possible paths are explored to find the destination.

```c++
#include <vector>
#include <queue>
#include <unordered_map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    bool validPath(int n, vector<vector<int>>& edges, int source, int destination) {
        // Step 1: Build the graph using an adjacency list
        unordered_map<int, vector<int>> graph;
        for (const vector<int>& edge : edges) {
            graph[edge[0]].push_back(edge[1]);
            graph[edge[1]].push_back(edge[0]);
        }
        
        // Step 2: Use BFS to determine if there is a path from source to destination
        queue<int> bfsQueue;
        unordered_set<int> visited;
        
        bfsQueue.push(source);
        visited.insert(source);
        
        while (!bfsQueue.empty()) {
            int current = bfsQueue.front();
            bfsQueue.pop();
            
            if (current == destination) {
                return true; // Found the destination
            }
            
            // Traverse all adjacent nodes
            for (int neighbor : graph[current]) {
                if (visited.find(neighbor) == visited.end()) {
                    visited.insert(neighbor);
                    bfsQueue.push(neighbor);
                }
            }
        }
        
        // If we exhaust the queue without finding the destination
        return false;
    }
};
```
## 752. Open the Lock
[752 LeetCode Link](https://leetcode.com/problems/open-the-lock/)

The problem at hand is a classic case of the shortest path search in an unweighted graph, where each node represents a state of the lock, and edges between nodes represent a valid move of one slot on one wheel. A BFS (Breadth-First Search) approach is suitable here due to its ability to find the shortest path in such scenarios.

- Treat each state of the lock as a node in a graph.
- Use BFS to explore all possible states from the initial state ('0000'), while avoiding deadends.
- For each state, generate all possible states that can be reached by turning one of the wheels one slot forward or backward.
- If we reach the target state, return the number of moves made.
- If we explore all possible moves without reaching the target, return -1.

Key considerations:

- We need to efficiently check for deadends and already visited states, hence we'll use a set for constant time complexity operations.
- Each state has 8 possible next states (each wheel can be moved forward or backward).
- Handle the wrap-around logic for wheel movements (from '9' to '0' and from '0' to '9').

### Python
Here is the Python code implementing the BFS solution:

```python3
from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        # Convert deadends to a set for quick lookup
        deadends = set(deadends)
        
        # Early exit if initial state is a deadend or target is the initial state
        if '0000' in deadends:
            return -1
        if target == '0000':
            return 0  # Immediate return since no moves are needed if target is initial
        
        # BFS setup
        queue = deque([('0000', 0)])  # (state, number of turns)
        visited = {'0000'}  # Visited states
        
        while queue:
            current, turns = queue.popleft()
            
            # Process all 8 possible moves (4 wheels x 2 directions)
            for i in range(4):
                # Calculate next and previous states for wheel at index i
                for step in (-1, 1):  # -1 for backward, 1 for forward
                    new_state = list(current)
                    new_state[i] = str((int(new_state[i]) + step) % 10)
                    new_state = ''.join(new_state)
                    
                    # Check if we've found the target
                    if new_state == target:
                        return turns + 1
                    
                    # Add new state to queue if it's not visited or a deadend
                    if new_state not in visited and new_state not in deadends:
                        visited.add(new_state)
                        queue.append((new_state, turns + 1))
        
        # If no solution found
        return -1
```

#### Understanding the Code
The goal is to determine the minimum moves required to reach a target combination from the starting combination '0000', avoiding any combinations listed as deadends.

- Initialization and Early Checks:
  - Convert the deadends list to a set to allow fast look-up times when checking if a state should be avoided.
  - Check if the initial state '0000' is a deadend. If it is, return -1 immediately because you can't start.
  - Check if the target is '0000'. If it is, return 0 because you are already at the target and no moves are needed.
- Breadth-First Search (BFS) Setup:
  - A queue is initialized with a tuple containing the initial state '0000' and the count of moves 0.
  - A set called visited is used to keep track of the combinations that have been already visited to avoid processing the same combination multiple times.
- BFS Loop:
  - The BFS loop begins by dequeuing the front element of the queue, which gives the current lock combination and the number of moves taken to reach this combination.
  - The loop then generates all possible states that can be reached from the current state by manipulating each of the four wheels individually:
  - Each wheel can be moved one step forward or one step backward. For example, moving from '0' to '9' (backward) or from '9' to '0' (forward) due to the circular nature of the wheels.
  - For each new state generated, the code does the following checks:
    - If this new state is the target, the function returns the current number of moves plus one (since we've made another move to reach this state).
    - If this new state has not been visited before and it's not a deadend, it's added to the visited set and enqueued in the queue with the incremented move count.
- End of Search:
- If the queue is exhausted and the target has not been reached, the function returns -1, indicating that the target cannot be reached without encountering a deadend.

> The solution uses a breadth-first search (BFS) to explore all possible combinations starting from '0000', level by level. This approach ensures that
> the first time a combination is reached, it's reached with the minimum number of moves possible. By processing combinations layer by layer and
> expanding outward from the initial state, the algorithm effectively finds the shortest path through the combinations that avoids deadends. The use of
> a queue ensures that combinations are explored in the order they're encountered, and the use of a set for visited prevents re-processing the same
> combination multiple times, enhancing efficiency.

## 1137. N-th Tribonacci Number
[1137 Leetcode Link](https://leetcode.com/problems/n-th-tribonacci-number)

For the Tribonacci sequence problem, we'll implement a solution that ensures optimal performance by leveraging dynamic programming (DP). The essence of the Tribonacci sequence is similar to the Fibonacci, but instead of summing the last two terms to get the next, we sum the last three.

Here's a concise breakdown of the approach:

- Initialization: Set up base values for T0, T1, and T2.
- Tabulation: Using a loop, calculate subsequent values based on the previous three, storing them in a list.
- Final Retrieval: Access the value for Tn directly from the list.

```pthyon3
class Solution:
    def tribonacci(self, n: int) -> int:
        # Base cases directly handled with a list
        if n == 0:
            return 0
        if n == 1 or n == 2:
            return 1
        
        # Tribonacci numbers up to n (space optimization: store only last three)
        t0, t1, t2 = 0, 1, 1
        
        # Compute each Tribonacci number from 3 to n
        for i in range(3, n + 1):
            # Current is the sum of the last three
            current = t0 + t1 + t2
            # Slide the window
            t0, t1, t2 = t1, t2, current
        
        # The nth Tribonacci number is now stored in t2
        return t2
```
### Explanation of the Solution:
- Initialization: We start by initializing t0, t1, and t2 for the base cases of the sequence.
- Tabulation Loop: From T3 onwards, each Tribonacci number is computed by summing up the three preceding values, and the previous numbers are then shifted accordingly.
- Memory Efficiency: Rather than maintaining a full list of Tribonacci numbers, only the three most recent numbers are stored. This is a form of space optimization common in DP solutions for sequences where only a few previous terms are required for the current computation.
- Return: After computing up to the desired Tn, it is simply returned from the variable holding the last computed value.
