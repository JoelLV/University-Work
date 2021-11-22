//Author: Joel Lopez Villarreal
//Version: 2.0

public class ArrayUtils{
    public static int maximum(int[] input) throws IllegalArgumentException{
        int i;
        int maximumValue = 0;
        
        if((input == null) || (input.length == 0)){
            throw new IllegalArgumentException("Invalid Input");
        }
        else{
            maximumValue = input[0];
            for(i = 1; i < input.length; ++i){
                if(maximumValue < input[i]){
                    maximumValue = input[i];
                    }
            }
            return maximumValue;
        }
    }
    public static boolean isAscending(int[] input){
        int i;
        boolean ascending = true;

        if(input == null){
            ascending = false;
            return ascending;
        }
        else if(input.length == 0){
            ascending = true;
            return ascending;
        }
        else{
            for(i = 0; i < (input.length - 1); ++i){
                if(input[i + 1] < input[i]){
                    ascending = false;
                    break;
                }
                else{

                }
            }
            return ascending;
        }
    }
    public static int[] filter(int[] Original, int[] deleteList){
        int i;
        int ii;
        int[] filteredArray;
        boolean nomatch = false;
        int numMatches = 0;
        int iii;

        if((Original == null) || (deleteList == null)){
            return null;
        }
        else{
            for(i = 0; i < Original.length; ++i){
                for(ii = 0; ii < deleteList.length; ++ii){
                    if(Original[i] == deleteList[ii]){
                        ++numMatches;
                        break;
                    }
                    else{

                    }
                }
            }
            filteredArray = new int[Original.length - numMatches];
            iii = 0;
            for(i = 0; i < Original.length; ++i){
                for(ii = 0; ii < deleteList.length; ++ii){
                    if(Original[i] == deleteList[ii]){
                        nomatch = false;
                        break;
                    }
                    else{
                        nomatch = true;
                    }
                }
                if(nomatch){
                    filteredArray[iii] = Original[i];
                    ++iii;
                }
            }
            return filteredArray;
        }
    }
    public static void rotateRight(int[] arrayToRotate, int rotations) throws IllegalArgumentException{
        int tempValue;
        int numRotations;
        int index;

            if(arrayToRotate == null){
                throw new IllegalArgumentException("Invalid input");
            }
            else{
                if(arrayToRotate.length == 0){

                }
                else if(rotations > 0){
                    for(numRotations = 0; numRotations < rotations; ++numRotations){
                        tempValue = arrayToRotate[arrayToRotate.length - 1];
                        for(index = 0; index < (arrayToRotate.length - 1); ++index){
                            arrayToRotate[arrayToRotate.length - 1 - index] = arrayToRotate[arrayToRotate.length - 2 - index];
                        }
                        arrayToRotate[0] = tempValue;
                    }
                    //System.out.println("New values in the Array:");
                }
                else if(rotations < 0){
                    for(numRotations = 0; numRotations < (Math.abs(rotations)); ++numRotations){
                        tempValue = arrayToRotate[0];
                        for(index = 0; index < (arrayToRotate.length - 1); ++index){
                            arrayToRotate[index] = arrayToRotate[index + 1];
                        }
                        arrayToRotate[arrayToRotate.length - 1] = tempValue;
                    }
                    //System.out.println("New values in the Array:");
                }
                else{

                }
                /*
                for(index = 0; index < arrayToRotate.length; ++index){
                    System.out.print(arrayToRotate[index] + " ");
                }
                */
            }
        }
    public static double[] rollingAverage(int[] Array, int interval) throws IllegalArgumentException{
        int i;
        double sum;
        double average;
        int ii;
        int iii;
        int repetitions;
        int limitRep;
        
            if(Array == null){
                throw new IllegalArgumentException("Invalid Input");
            }
            else if((Array.length == 0) || (interval > Array.length) || (interval < 1)){
                throw new IllegalArgumentException("Invalid Input");
            }
            else{
                sum = 0.0;
                limitRep = (Array.length - interval + 1);
                iii = 0;
                i = 0;
                double[] averageArray = new double[limitRep];
                for(repetitions = 0; repetitions < limitRep; ++repetitions){
                    i = repetitions;
                    for(ii = 0; ii < (interval - 1); ++ii){
                        sum = sum + (double)Array[i];
                        ++i;
                    }
                    sum = sum + (double)Array[i];
                    average = sum / (double)interval;
                    averageArray[iii] = average;
                    ++iii;
                    sum = 0.0;
                }
                return averageArray;
            }
        }
}
