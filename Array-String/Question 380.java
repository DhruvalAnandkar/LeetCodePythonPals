/*
380. Insert Delete GetRandom O(1)
Medium
Topics
Companies

Implement the RandomizedSet class:

    RandomizedSet() Initializes the RandomizedSet object.
    bool insert(int val) Inserts an item val into the set if not present. Returns true if the item was not present, false otherwise.
    bool remove(int val) Removes an item val from the set if present. Returns true if the item was present, false otherwise.
    int getRandom() Returns a random element from the current set of elements (it's guaranteed that at least one element exists when this method is called). Each element must have the same probability of being returned.

You must implement the functions of the class such that each function works in average O(1) time complexity.

*/

import java.util.*;

class RandomizedSet {
    HashMap<Integer, Integer> locset; 
    int[] tset;

    public RandomizedSet() {
        locset = new HashMap<Integer, Integer>();
        tset = new int[0];
    }
    
    public boolean insert(int val) {
        if (locset.containsKey(val)) {
            return false;
        } else {
            tset = Arrays.copyOf(tset, tset.length + 1);
            tset[tset.length - 1] = val;
            locset.put(val, tset.length - 1);
            return true;
        }
    }
    
    public boolean remove(int val) {
        if (!locset.containsKey(val)) {
            return false;
        } else {
        	int t = locset.get(val);
            tset[t] = tset[tset.length - 1];
            locset.put(tset[t], t);
            tset = Arrays.copyOf(tset, tset.length - 1);
            locset.remove(val);
            return true;
        }       
    }
    
    public int getRandom() { 
        Random r = new Random();
        int i = r.nextInt(tset.length);
        return tset[i];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * RandomizedSet obj = new RandomizedSet();
 * boolean param_1 = obj.insert(val);
 * boolean param_2 = obj.remove(val);
 * int param_3 = obj.getRandom();
 */
