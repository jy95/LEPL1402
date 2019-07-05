package BlackBox.flavour;

import BlackBox.BinarySearchFlavour;
import BlackBox.FlavourExercise;

public class BinarySearchErr1 extends BinarySearchFlavour implements FlavourExercise {

    private static final boolean correctness = false;

    @Override
    public int binarySearch(int [] arr, int low, int high, int elem) {

        if(low > high || low < 0 || high > arr.length-1){
            return -2;
        }

        while (high > low) { // mistake is here

            int mid = (low + high) / 2;

            if (arr[mid] == elem){
                return mid;
            }

            if (arr[mid] > elem){
                high = mid - 1;
            } else {
                low = mid + 1;
            }

        }

        // not found.
        return -1;
    }

    @Override
    public boolean correctness() {
        return correctness;
    }


    public static void main(String [] args){

    }
}