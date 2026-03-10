import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.ArrayDeque;
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



public class PrintAllPathUsingBFS{
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

        printAllPathFromIdx(graph, startIdx);

    }

    static class IdxAndPathSoFar{
        int idx;
        String pathSoFar;

        public IdxAndPathSoFar(int idx, String pathSoFar){
            this.idx = idx;
            this.pathSoFar = pathSoFar;
        }
    }

    static void printAllPathFromIdx(ArrayList<Edge> graph[], int startIdx){
        
        
        boolean[] isVisited = new boolean[graph.length];
        
        ArrayDeque<IdxAndPathSoFar> toVisit = new ArrayDeque<>();
        toVisit.add(new IdxAndPathSoFar(startIdx, "" + startIdx));

        while (toVisit.size() > 0) {
            
            // remove
            IdxAndPathSoFar curIdxAndPathSoFar = toVisit.pop();
            int curIdx = curIdxAndPathSoFar.idx;
            String curPathSoFar = curIdxAndPathSoFar.pathSoFar;

            // check if already visited, then continue
            if(isVisited[curIdx]) continue;

            // If not visited , do your current work
            System.out.println(curIdx +"@" + curPathSoFar);
            isVisited[curIdx] = true;

            // Add it's neighbours to the queue only if they are not visited yet
            for( Edge e: graph[curIdx] ){
                if(!isVisited[e.dest]){
                    toVisit.add(  new IdxAndPathSoFar( e.dest, curPathSoFar + e.dest ) );
                }
            }

        }

    }

}