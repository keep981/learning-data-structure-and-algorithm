import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Scanner;
import java.io.IOException;

class Edge{
    int src;
    int dest;
    int wt;
    public Edge(int src, int dest, int wt){
        this.src = src;
        this.dest = dest;
        this.wt = wt;
    }
}

public class GetConnectedComponents{
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader( new InputStreamReader( System.in )  );
        int vertices = Integer.parseInt(br.readLine()  );

        ArrayList<Edge>[] graph = new ArrayList[vertices];

        for(int i =0; i < vertices; i++){
            graph[i] = new ArrayList<>();
        }
        
        int edges = Integer.parseInt(br.readLine());
        for(int i =0; i< edges; i ++){
            String[] tokens = br.readLine().split(" ");
            int v1 = Integer.parseInt(tokens[0]);
            int v2 = Integer.parseInt(tokens[1]);
            int wt = Integer.parseInt(tokens[2]);
            graph[v1].add( new Edge(v1, v2, wt) );
            graph[v2].add( new Edge(v2, v1, wt) );
        }
        
        boolean[] isVisited = new boolean[vertices];
        StringBuilder pathTillNow = new StringBuilder();
        ArrayList<ArrayList<Integer>> connectedComponents = getConnectedComponentsHelper(graph);

        for(ArrayList<Integer> component: connectedComponents){
            for(Integer idx: component){
                System.out.print( idx + ", " );
            }
            System.out.println();
        }

    }
    static ArrayList<ArrayList<Integer>> getConnectedComponentsHelper(ArrayList<Edge> graph[]){
        
        ArrayList<ArrayList<Integer>> connectedComponents = new ArrayList<>();
        boolean[] isVisited = new boolean[graph.length];
        for(int i =0; i < graph.length; i++){
            if( ! isVisited[i] ){
                ArrayList<Integer> component = new ArrayList<>();
                getConnectedComponents(graph, i, isVisited, component);
                connectedComponents.add(component);
            }      
        }

        return connectedComponents;
    }
    static void getConnectedComponents(ArrayList<Edge> graph[], int src, boolean[] isVisited, ArrayList<Integer> component){

        component.add(src);
        isVisited[src] = true;
        for(Edge edgeItr: graph[src]){
            if( !isVisited[edgeItr.dest] ){
                getConnectedComponents(graph, edgeItr.dest, isVisited, component);
            }
        }
    }

}