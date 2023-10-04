        import java.util.*;
        import java.io.*;

        class curr_edge implements Comparable<curr_edge> {
            int curr_src, curr_dest;
            double curr_weight;

            public curr_edge(int curr_src, int curr_dest, double curr_weight) {
                this.curr_src = curr_src;
                this.curr_dest = curr_dest;
                this.curr_weight = curr_weight;
            }

            @Override
            public int compareTo(curr_edge curr_edge) {
                return Double.compare(this.curr_weight, curr_edge.curr_weight);
            }
        }

        public class minSPT {
            public static void main(String[] args) {
                if (args.length != 1) {
                    System.out.println("Usage: java minSPT <input_file>");
                    return;
                }

                String inputFile = args[0];

                try (BufferedReader br = new BufferedReader(new FileReader(inputFile))) {
                    List<Set<curr_edge>> graphs = new ArrayList<>();

                    String line;
                    while ((line = br.readLine()) != null) {
                        if (line.startsWith("** G")) {
                            Set<curr_edge> curr_edges = new HashSet<>();

                            while ((line = br.readLine()) != null && !line.equals("---------------- ")) {
                                if (line.trim().startsWith("(") && !line.trim().startsWith("(u, v, w)")) {
                                    String[] parts = line.trim().substring(1, line.trim().length() - 1).split(",");
                                    if (parts.length != 3) continue;

                                    try {
                                        int curr_src = Integer.parseInt(parts[0].trim());
                                        int curr_dest = Integer.parseInt(parts[1].trim());
                                        String curr_weightStr = parts[2].trim().replaceAll("[^\\d.]", "");
                                        double curr_weight = Double.parseDouble(curr_weightStr);
                                        curr_edges.add(new curr_edge(curr_src, curr_dest, curr_weight));
                                    } catch (NumberFormatException e) {
                                        System.err.println("Error parsing line: " + line);
                                    }
                                }
                            }

                            graphs.add(curr_edges);
                        }
                    }

                    for (int i = 0; i < graphs.size(); i++) {
                        System.out.println("** G" + (i + 1) + ":");
                        curr_edge[] sorted_curr_edges = graphs.get(i).toArray(new curr_edge[0]);
                        Arrays.sort(sorted_curr_edges);

                        kruskalMST(i + 1, sorted_curr_edges);
                        primMST(i + 1, graphs.get(i));
                    }
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }

            public static void kruskalMST(int curr_graphNumber, curr_edge[] sorted_curr_edges) {
                System.out.println("Kruskal`s algorithm for Graph " + curr_graphNumber + ":");

                int[] curr_parent = new int[sorted_curr_edges.length + 1];
                Arrays.fill(curr_parent, -1);
                ArrayList<curr_edge> min_spann_tree = new ArrayList<>();
                double totalcurr_weight = 0.0;

                for (curr_edge curr_edge : sorted_curr_edges) {
                    int curr_srcRoot = find(curr_parent, curr_edge.curr_src);
                    int curr_destRoot = find(curr_parent, curr_edge.curr_dest);

                    if (curr_srcRoot != curr_destRoot) {
                        min_spann_tree.add(curr_edge);
                        totalcurr_weight += curr_edge.curr_weight;
                        union(curr_parent, curr_srcRoot, curr_destRoot);
                    }
                }

                for (curr_edge curr_edge : min_spann_tree) {
                    System.out.println("(" + curr_edge.curr_src + ", " + curr_edge.curr_dest + ", " + curr_edge.curr_weight + ")");
                }

                System.out.println("==> Total curr_weight " + totalcurr_weight+"\n");
            }

            private static int find(int[] curr_parent, int vertex) {
                if (curr_parent[vertex] == -1) return vertex;
                return find(curr_parent, curr_parent[vertex]);
            }

            private static void union(int[] curr_parent, int x, int y) {
                int xRoot_graph = find(curr_parent, x);
                int yRoot_graph = find(curr_parent, y);
                curr_parent[xRoot_graph] = yRoot_graph;
            }

            public static void primMST(int curr_graphNumber, Set<curr_edge> curr_edges) {
                System.out.println("Prim`s algorithm for Graph " + curr_graphNumber + ":");
            
                int num_Vertices_graph = curr_edges.size() + 1;
                int[] curr_parent = new int[num_Vertices_graph];
                Arrays.fill(curr_parent, -1);
                double[] key_value = new double[num_Vertices_graph];
                Arrays.fill(key_value, Double.MAX_VALUE);
                boolean[] curr_in_MST = new boolean[num_Vertices_graph];
                double totalcurr_weight = 0.0;
            
                key_value[0] = 0;
            
                for (int count = 0; count < num_Vertices_graph - 1; count++) {
                    int u = minKey(key_value, curr_in_MST);
                    if (u == -1) {
                        break;
                    }
                    curr_in_MST[u] = true;
            
                    for (curr_edge curr_edge : curr_edges) {
                        int v = -1;
                        double weight = curr_edge.curr_weight;
            
                        if (curr_edge.curr_src == u && !curr_in_MST[curr_edge.curr_dest]) {
                            v = curr_edge.curr_dest;
                        } else if (curr_edge.curr_dest == u && !curr_in_MST[curr_edge.curr_src]) {
                            v = curr_edge.curr_src;
                        }
            
                        if (v != -1 && weight < key_value[v]) {
                            curr_parent[v] = u;
                            key_value[v] = weight;
                        }
                    }
                }
            
                for (int i = 1; i < num_Vertices_graph; i++) {
                    if (key_value[i] != Double.MAX_VALUE) {
                        System.out.println("(" + curr_parent[i] + ", " + i + ", " + key_value[i] + ")");
                        totalcurr_weight += key_value[i];
                    }
                }
            
                System.out.println("==> Total curr_weight " + totalcurr_weight);
            }
            

            private static int minKey(double[] key_value, boolean[] curr_in_MST) {
                double min = Double.MAX_VALUE;
                int min_curr_index = -1;

                for (int v = 0; v < key_value.length; v++) {
                    if (!curr_in_MST[v] && key_value[v] < min) {
                        min = key_value[v];
                        min_curr_index = v;
                    }
                }

                return min_curr_index;
            }
        }
