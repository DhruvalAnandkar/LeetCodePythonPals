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


//WIP
class RandomizedSet {
    int[] tset; //holds all nums, 0 index isn't used [x, 1, -3, 4, 77...]
    int[] pset; //holds pos num index in tset, 0 for not present: [1, 0, 0, 4...]
    int[] nset; //holds non-pos num index in tset, 0 for not present: [0, 0, 0, 3...]

    //below values are an attempt to reduce memory used by shrinking the pset/nset arrays to the smallest size needed
    int phigh; //biggest magnitude pos num (default: 0)
    int p2ndhigh; //2nd biggest pos mag
    int nhigh; //biggest magnitude neg num (default: -1)
    int n2ndhigh; //2nd biggest neg mag

    public RandomizedSet() {
        tset = new int[1];
        pset = new int[0];
        nset = new int[0];
        phigh = 0;
        p2ndhigh = 0;
        nhigh = -1;
        n2ndhigh = -1;

    }
    
    public boolean insert(int val) {
        if (val > 0) {
            if (val > pset.length) pset = Arrays.copyOf(pset, val);
            if (pset[val - 1] == 0) {
                pset[val - 1] = tset.length;
                tset = Arrays.copyOf(tset, tset.length + 1);
                tset[tset.length - 1] = val;
                if (val > phigh) {
                    p2ndhigh = phigh;
                    phigh = val;
                }
                return true;
            } else {
                return false;
            }
        } else {
            if ((val * -1) + 1 > nset.length) nset = Arrays.copyOf(nset, (val * -1) + 1);
            if (nset[(val * -1)] == 0) {
                nset[(val * -1)] = tset.length;
                tset = Arrays.copyOf(tset, tset.length + 1);
                tset[tset.length - 1] = val;
                if (val * -1 > nhigh) {
                    n2ndhigh = nhigh;   
                    nhigh = (val * -1);
                }
                return true;
            } else {
                return false;
            }
        }
    }
    
    public boolean remove(int val) {
        if (val > 0) {
            if ((val > pset.length) || (pset[val - 1] == 0)) {
                return false;
            } else {
                if (tset[tset.length - 1] > 0) {
                    pset[tset[tset.length - 1] - 1] = pset[val - 1]; 
                } else {
                    nset[tset[tset.length - 1] * -1] = pset[val - 1];
                }
                
                tset[pset[val - 1]] = tset[tset.length - 1];
                tset = Arrays.copyOf(tset, tset.length - 1);
                pset[val - 1] = 0;
                if (val == phigh) phigh = p2ndhigh;
                pset = Arrays.copyOf(pset, phigh);
                return true;
            }
        } else {
            if (((val * -1) + 1 > nset.length) || (nset[(val * -1)] == 0)) {
                return false;
            } else {
                if (tset[tset.length - 1] > 0) {
                    pset[tset[tset.length - 1] - 1] = nset[val * -1]; 
                } else {
                    nset[tset[tset.length - 1] * -1] = nset[val * -1];
                }

                tset[nset[(val * -1)]] = tset[tset.length - 1];
                tset = Arrays.copyOf(tset, tset.length - 1);
                nset[(val * -1)] = 0;
                if (val == nhigh * -1) nhigh = n2ndhigh;
                nset = Arrays.copyOf(nset, nhigh + 1);
                return true;
            }
        }       
    }
    
    public int getRandom() { 
        Random r = new Random();
        int i = r.nextInt(tset.length - 1) + 1;
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
