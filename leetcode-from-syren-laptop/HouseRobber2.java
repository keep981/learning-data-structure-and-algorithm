class Solution {
    public static int rob(int[] nums) {
        
        int len = nums.length;
        for(int x:nums)
            System.out.print( x+ "->" );
        System.out.println();

        if(len == 1 ){
            return nums[0];
        }
        else if(len == 2){
            return Math.max(nums[0], nums[1]   );
        }
        else if(len == 3){
            return Math.max(nums[0], Math.max (nums[1], nums[2]) );
        }
        int[] maxTheft = new int[ len ];
        boolean[] usedLastHouse = new boolean[ len ];

        
        maxTheft[ len -1 ] =    nums [ len - 1 ];
        usedLastHouse[ len -1 ] =   true;

        maxTheft[ len - 2 ] =    nums [ len - 2 ];
        usedLastHouse[ len - 2 ] =    false;

        maxTheft[ len - 3 ] =    nums [ len - 3 ]  + maxTheft[  len -1  ] ;
        usedLastHouse[ len - 3 ] =   true;


        for( int i= len - 4; i>0 ; i--){   //for first element we will calculate later
            if(maxTheft[i + 2]  == maxTheft[i + 3]){
                // System.out.println("Within equal");
                maxTheft[i] = nums[i] + maxTheft[i + 2];
                usedLastHouse[ i ] =   false; //0th idx ku use karibaku sahaj haba
            }
            else if(maxTheft[i + 2]  > maxTheft[i + 3]){
                // System.out.println("Within greater");
                maxTheft[i] = nums[i] + maxTheft[i + 2];
                usedLastHouse[ i ] =   usedLastHouse[i + 2];
            }
            else{
                // System.out.println("Within less");
                maxTheft[i] = nums[i] + maxTheft[i + 3];
                usedLastHouse[ i ] =   usedLastHouse[i + 3];
            }
        }


        int _0th_indexMaximaSubProblemFirst = nums[0] + maxTheft[2];
        if(usedLastHouse[ 0 + 2 ]){

            _0th_indexMaximaSubProblemFirst = _0th_indexMaximaSubProblemFirst - Math.min( nums[0], nums[ len -1]   );
        }

        int _0th_indexMaximaSubProblemSecond = nums[0] + maxTheft[3];
        if(usedLastHouse[ 0 + 3 ]){

            _0th_indexMaximaSubProblemSecond = _0th_indexMaximaSubProblemSecond - Math.min( nums[0], nums[ len -1]   );
        }

        
        for(int x:maxTheft)
            System.out.print( x+ "->" );
        System.out.println();
        for(boolean x:usedLastHouse)
            System.out.print( x+ "->" );
        System.out.println();


        return Math.max(_0th_indexMaximaSubProblemFirst, Math.max(_0th_indexMaximaSubProblemSecond, maxTheft[1])   );

    }

    public static void main(String args[]){
        // int[] arr = {1,2,3,1};
        // int[] arr = {200,3,140,20,10};
        // int[] arr = {8,2,8,9,2};
        int[] arr = {8,4,8,5,9,6,5,4,4,10};

        

        System.out.println( "ans="+rob(arr) );
    }
    
}