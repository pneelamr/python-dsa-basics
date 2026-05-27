# DSA Reference Implementations

Procedural Python implementations of common data structures and algorithms — no OOP, no external libraries, plain Python types throughout.

Each file follows a consistent format:
- 3-line description of the concept
- `# Time:` and `# Space:` complexity comments above every function
- One topic per file, named `basic_<topic>.py`

## Data Structures (24)

| File | Description |
|------|-------------|
| `basic_array.py` | Fixed-size sequential collection accessed by index |
| `basic_stack.py` | LIFO — push/pop from the same end |
| `basic_queue.py` | FIFO — enqueue at back, dequeue from front |
| `basic_deque.py` | Double-ended queue — O(1) insert/remove at both ends |
| `basic_circular_queue.py` | Fixed-capacity queue with wrap-around pointers |
| `basic_priority_queue.py` | Queue ordered by priority using heapq |
| `basic_set.py` | Unordered unique elements backed by Python set |
| `basic_hash_table.py` | Key-value store with chaining for collision resolution |
| `basic_singly_linked_list.py` | Chain of nodes with a next pointer |
| `basic_doubly_linked_list.py` | Chain of nodes with next and previous pointers |
| `basic_circular_linked_list.py` | Singly linked list where tail points back to head |
| `basic_binary_tree.py` | Hierarchical structure with at most two children per node |
| `basic_tree.py` | General tree with any number of children per node |
| `basic_avl_tree.py` | Self-balancing BST with height-difference ≤ 1 |
| `basic_heap.py` | Min-heap via heapq |
| `basic_heap_array.py` | Min-heap built from scratch on a plain list |
| `basic_graph.py` | Adjacency list graph |
| `basic_adjacency_matrix.py` | Dense graph as a 2D list |
| `basic_trie.py` | Prefix tree for string storage and lookup |
| `basic_disjoint_set.py` | Union-Find with path compression and union by rank |
| `basic_segment_tree.py` | Range query and point update in O(log n) |
| `basic_fenwick_tree.py` | Prefix-sum queries and updates in O(log n) |
| `basic_sparse_matrix.py` | Sparse matrix stored as dict of (row, col) → value |
| `basic_lru_cache.py` | Least-recently-used cache with O(1) get and put |
| `basic_bloom_filter.py` | Probabilistic membership with tunable false-positive rate |

## Sorting (10)

| File | Complexity |
|------|------------|
| `basic_bubble_sort.py` | O(n²) |
| `basic_selection_sort.py` | O(n²) |
| `basic_insertion_sort.py` | O(n²) avg, O(n) best |
| `basic_shell_sort.py` | O(n log² n) |
| `basic_merge_sort.py` | O(n log n) |
| `basic_quick_sort.py` | O(n log n) avg |
| `basic_heap_sort.py` | O(n log n) |
| `basic_counting_sort.py` | O(n + k) |
| `basic_radix_sort.py` | O(d × (n + k)) |
| `basic_bucket_sort.py` | O(n + k) avg |

## Searching (5)

| File | Complexity |
|------|------------|
| `basic_linear_search.py` | O(n) |
| `basic_binary_search.py` | O(log n) |
| `basic_jump_search.py` | O(√n) |
| `basic_interpolation_search.py` | O(log log n) avg |
| `basic_exponential_search.py` | O(log n) |

## Graph Algorithms (9)

| File | Description |
|------|-------------|
| `basic_bfs.py` | Breadth-first traversal |
| `basic_dfs.py` | Depth-first traversal |
| `basic_dijkstra.py` | Single-source shortest path (non-negative weights) |
| `basic_bellman_ford.py` | Single-source shortest path (handles negative weights) |
| `basic_a_star.py` | Heuristic shortest path |
| `basic_floyd_warshall.py` | All-pairs shortest path |
| `basic_kruskal.py` | Minimum spanning tree — sort edges |
| `basic_prim.py` | Minimum spanning tree — grow from vertex |
| `basic_topological_sort.py` | Linear ordering of a DAG |

## Dynamic Programming (10)

| File | Description |
|------|-------------|
| `basic_fibonacci.py` | Memoization and tabulation |
| `basic_knapsack.py` | 0/1 knapsack |
| `basic_lcs.py` | Longest common subsequence |
| `basic_lis.py` | Longest increasing subsequence |
| `basic_coin_change.py` | Minimum coins / total ways |
| `basic_edit_distance.py` | Levenshtein distance |
| `basic_matrix_chain.py` | Optimal matrix chain parenthesization |
| `basic_rod_cutting.py` | Maximum revenue from rod cuts |
| `basic_subset_sum.py` | Subset summing to target |
| `basic_palindrome_partitioning.py` | Minimum palindrome cuts |

## String Algorithms (10)

| File | Description |
|------|-------------|
| `basic_naive_pattern_search.py` | Brute-force O(n×m) |
| `basic_kmp.py` | Knuth-Morris-Pratt — O(n+m) |
| `basic_rabin_karp.py` | Rolling hash pattern search |
| `basic_boyer_moore.py` | Bad-character heuristic |
| `basic_z_algorithm.py` | Z-array linear pattern match |
| `basic_anagram.py` | Frequency-based anagram check and window search |
| `basic_palindrome.py` | Palindrome check variants |
| `basic_string_reversal.py` | Reverse string, words, in-place |
| `basic_longest_palindromic_substring.py` | Expand-around-center and DP |
| `basic_run_length_encoding.py` | RLE compress and decompress |

## Backtracking (11)

| File | Description |
|------|-------------|
| `basic_n_queens.py` | N non-attacking queens on N×N board |
| `basic_sudoku.py` | 9×9 Sudoku solver |
| `basic_rat_in_maze.py` | All paths through a grid |
| `basic_subsets.py` | Power set enumeration |
| `basic_permutations.py` | All orderings of a sequence |
| `basic_combinations.py` | k-combinations and subset sum |
| `basic_word_search.py` | Word in a 2D character grid |
| `basic_graph_coloring.py` | k-color assignment with no adjacent conflicts |
| `basic_hamiltonian_path.py` | Visit every vertex exactly once |
| `basic_knights_tour.py` | Knight visits every chessboard square once |

## Greedy (5)

| File | Description |
|------|-------------|
| `basic_activity_selection.py` | Maximum non-overlapping intervals |
| `basic_fractional_knapsack.py` | Knapsack with fractional items |
| `basic_huffman_coding.py` | Optimal prefix-free compression codes |
| `basic_job_sequencing.py` | Maximize profit subject to deadlines |
| `basic_minimum_platforms.py` | Minimum railway platforms needed |

## Two Pointers & Sliding Window (5)

| File | Description |
|------|-------------|
| `basic_two_pointers.py` | Two-sum, three-sum, container water, trapping rain |
| `basic_kadane.py` | Maximum subarray (including circular variant) |
| `basic_sliding_window.py` | Fixed-size window — max/min sum |
| `basic_longest_substring_unique.py` | Variable window — unique chars, k-distinct, min window |
| `basic_sliding_window_max.py` | Per-window max/min via monotonic deque |

## Divide & Conquer (4)

| File | Description |
|------|-------------|
| `basic_binary_exponentiation.py` | base^exp in O(log exp) |
| `basic_closest_pair.py` | Closest pair of points in O(n log n) |
| `basic_karatsuba.py` | Integer multiplication in O(n^1.585) |
| `basic_strassen.py` | Matrix multiplication in O(n^2.807) |

## Math & Number Theory (5)

| File | Description |
|------|-------------|
| `basic_gcd_lcm.py` | Euclidean GCD, LCM, extended GCD |
| `basic_sieve.py` | Sieve of Eratosthenes, segmented sieve |
| `basic_prime_factorization.py` | Trial division factorization and primality test |
| `basic_modular_arithmetic.py` | Modular exponentiation, inverse, CRT |
| `basic_catalan_number.py` | Catalan numbers via DP and closed form |

## Bit Manipulation (3)

| File | Description |
|------|-------------|
| `basic_bit_manipulation.py` | Get, set, clear, toggle individual bits |
| `basic_bit_tricks.py` | Kernighan bit count, XOR tricks, power of 2 |
| `basic_bitmask.py` | Subset enumeration, bitmask DP (TSP) |

## Advanced Graph (6)

| File | Description |
|------|-------------|
| `basic_tarjan.py` | Strongly connected components (single DFS) |
| `basic_kosaraju.py` | Strongly connected components (two DFS passes) |
| `basic_articulation_points.py` | Articulation points and bridges |
| `basic_eulerian_path.py` | Eulerian path/circuit via Hierholzer's |
| `basic_bipartite.py` | 2-colorability check |
| `basic_cycle_detection.py` | Floyd's tortoise-and-hare, DFS cycle detection |

## Advanced Strings (4)

| File | Description |
|------|-------------|
| `basic_suffix_array.py` | Sorted suffix indices + LCP array |
| `basic_aho_corasick.py` | Multi-pattern matching automaton |
| `basic_manacher.py` | All palindromic substrings in O(n) |
| `basic_string_hashing.py` | Polynomial rolling hash for O(1) substring comparison |
