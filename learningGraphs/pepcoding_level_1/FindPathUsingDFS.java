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

public class FindPathUsingDFS{
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
        
        int startIdx = Integer.parseInt(br.readLine());
        int endIdxIdx = Integer.parseInt(br.readLine());

        printMyGraph(graph);
        
        boolean[] isVisited = new boolean[vertices];
        boolean ans = isPathExists(graph, startIdx, endIdxIdx, isVisited);
        
        System.out.println( String.format("From startIdx=%d to endIdx =%d, got answer for isPathExists=%b", 
            startIdx, endIdxIdx, ans
        ) );
    }

    static boolean isPathExists(ArrayList<Edge> graph[], int startIdx, int endIdx, boolean[] isVisited){
        
        if(startIdx == endIdx)
            return true;
        
        isVisited[startIdx] = true;

        for( Edge edgeItr : graph[startIdx]){
            if( isVisited[edgeItr.dest] )
                continue;

            boolean subProbAns = isPathExists(graph, edgeItr.dest, endIdx, isVisited);
            if(subProbAns){
                return true;
            }
        }
        return false;
    }

    static void printMyGraph(ArrayList<Edge>[] g){
        for(int i =0 ; i < g.length; i++){
            for(Edge e : g[i]){
                System.out.println( e.wt + "<-->" );
            }
        }
    }
}