import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class FindPerfectFriends {
    public static void main(String[] args) throws Exception {
        
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in )  );
        int noOfStudents = Integer.parseInt(br.readLine());

        ArrayList<Edge>[] graph = new ArrayList[noOfStudents];

        for(int i =0; i < noOfStudents; i++){
            graph[i] = new ArrayList<>();
        }
        
        int noOfFriendshipLines = Integer.parseInt(br.readLine());
        for(int i =0; i< noOfFriendshipLines; i ++){
            String[] tokens = br.readLine().split(" ");
            int v1 = Integer.parseInt(tokens[0]);
            int v2 = Integer.parseInt(tokens[1]);
            // int wt = Integer.parseInt(tokens[2]);
            graph[v1].add( new Edge(v1, v2, -1) );
            graph[v2].add( new Edge(v2, v1, -1) );
        }

        int ans = findNumberOfStudentPairBelongsToDifferentClubs(graph);
        System.out.println( "Got answer = " + ans );
    }

    public static int findNumberOfStudentPairBelongsToDifferentClubs( ArrayList<Edge>[] graph  ){
        
        ArrayList<ArrayList<Integer>> connectedComponents = getConnectedComponentsHelper(graph);
        
        for( ArrayList<Integer> component : connectedComponents ){

            for(int vertex : component){
                System.out.print( vertex + ", " );
            }
            System.out.println();
        }
        
        int numberOfStudentPairBelongsToDifferentClubs = 0;
        // Now to compute the count we have to take the multiplication of size of each groups with other
        for(int i =0; i < connectedComponents.size(); i++  ){
            for(int j = i + 1; j < connectedComponents.size() ; j++){
                numberOfStudentPairBelongsToDifferentClubs += (connectedComponents.get(i).size() * connectedComponents.get(j).size());
            }
        }
        return numberOfStudentPairBelongsToDifferentClubs;
    }

    public static ArrayList<ArrayList<Integer>> getConnectedComponentsHelper( ArrayList<Edge>[] graph ){
        
        ArrayList<ArrayList<Integer>> connectedComponents = new ArrayList<>();
        boolean[] isVisited = new boolean[ graph.length ];
        for(int i =0; i<graph.length; i++){
            if( !isVisited[ i ] ){
                ArrayList<Integer> component = new ArrayList<>();
                getConnectedComponents(graph, i, isVisited, component);
                connectedComponents.add(component);
            }
        }

        return connectedComponents;

    }

    public static void getConnectedComponents( ArrayList<Edge>[] graph, int vertexIdx, boolean[] isVisited, ArrayList<Integer> component){

        isVisited[vertexIdx] = true;
        component.add(vertexIdx);

        for(Edge ed :graph[vertexIdx] ){
            if( !isVisited[ ed.dest ] ){
                getConnectedComponents(graph, ed.dest, isVisited, component);
            }

        }

    }

}
