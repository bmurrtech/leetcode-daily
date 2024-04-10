## 2073. Time Needed to Buy Tickets

![2073](https://i.imgur.com/knSllgu.png)

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
![950](https://i.imgur.com/qBohtPh.png)

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
