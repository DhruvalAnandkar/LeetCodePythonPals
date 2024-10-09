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


class RandomizedSet {
    boolean[] pset = new int[0];
    boolean[] nset = new int[0]; //also holds 0

    public RandomizedSet() {
        pset = new int[0];
        nset = new int[0];
    }
    
    public boolean insert(int val) {
        if (val >0) {
            if (val > pset.length) {
                pset = Arrays.copyOf(pset, val);
                pset[val - 1] = true;
            } else if (pset[val] == null) {
                pset[val - 1] = true;
            } else {
                return false;
            }
        } else {
            if ((val * -1) >= pset.length) {
                pset = Arrays.copyOf(pset, val);
                pset[(val * -1)] = true;
            } else if (pset[val] == null) {
                pset[val * -1] = true;
            } else {
                return false;
            }
        }
    }
    
    public boolean remove(int val) {
        if (val > 0) {
            if (val > pset.length) {
                return false;
            } else if (pset[val] == null) {
                return false;
            } else {
                pset[val - 1] = false;
                return true;
            }
        }else {
            if ((val * -1) >= pset.length) {
                return false;
            } else if (pset[val] == null) {
                return false;
            } else {
                pset[val * -1] = false;
                return true;
            }
        }       
    }
    
    public int getRandom() {
        
    }
}
