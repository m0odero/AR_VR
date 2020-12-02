using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class MyScript: MonoBehaviour
{
    public Mesh my_mesh;

    // class member variables
    public Vector3[] newVertices;
    public int[] newTriangles;
    public Vector2[] my_UV;

    // sides is the length of one side of the mesh
    // no_of_vertices is the number of triangle vertices in the mesh
    // no_of_vertices = (sides * 2) * 3
    public int sides          = 100;
    public int no_of_vertices = 60000;

    // Start is called before the first frame update
    void Start()
    {
        my_mesh      = new Mesh();
        
        // initializing the arrays 
        newVertices  = new Vector3[no_of_vertices];
        newTriangles = new int[no_of_vertices];
        my_UV        = new Vector2[no_of_vertices];
        
        int k = 0;
         for (int i = 0; i < sides; i++)
         {
           for (int j = 0; j < sides; j++)
           {
             // (x,y), (x1,y), (x,y1), (x1,y1) are the four vertices in a square
             // each square produces two triangles hence six vertices
             // (u,v), (u1,v), (u,v1), (u1,v1) are the coordinates of the texture image

               float x  = (float)((float)(-2.5) + ((float)i    * 1.0/(float)20));
               float y  = (float)((float)(-2.5) + ((float)j    * 1.0/(float)20));
               float x1 = (float)((float)(-2.5) + (float)(i+1) * (1.0/(float)20));
               float y1 = (float)((float)(-2.5) + (float)(j+1) * (1.0/(float)20));
               
               float u  = (float)((float)i     * (1.0/(float)sides));
               float v  = (float)((float)j     * (1.0/(float)sides));
               float u1 = (float)((float)(i+1) * (1.0/(float)sides));
               float v1 = (float)((float)(j+1) * (1.0/(float)sides));

               newVertices[k]   = new Vector3(x,y,0);
               newVertices[k+1] = new Vector3(x1,y,0);
               newVertices[k+2] = new Vector3(x,y1,0);

               newTriangles[k]   = k;
               newTriangles[k+1] = k+1;
               newTriangles[k+2] = k+2;

               my_UV[k]   = new Vector2(-u,v);
               my_UV[k+1] = new Vector2(-u1,v);
               my_UV[k+2] = new Vector2(-u,v1);
    

               newVertices[k+3] = new Vector3(x1,y1,0);
               newVertices[k+4] = new Vector3(x,y1,0);
               newVertices[k+5] = new Vector3(x1,y,0);
               
               newTriangles[k+3] = k+3;
               newTriangles[k+4] = k+4;
               newTriangles[k+5] = k+5;
                              
               my_UV[k+3] = new Vector2(-u1,v1);
               my_UV[k+4] = new Vector2(-u,v1);
               my_UV[k+5] = new Vector2(-u1,v);
               
               k = k+6;
           }  
         }
         
         my_mesh.Clear();

         my_mesh.vertices  = newVertices;
         my_mesh.triangles = newTriangles;
         my_mesh.uv        = my_UV;

         my_mesh.RecalculateNormals();
         my_mesh.RecalculateBounds();
         GetComponent<MeshFilter>().mesh = my_mesh; 
    }

    // Update is called once per frame
    void Update()
    {
        float t = Time.time;
        int a = 10;
                 
             for (int i = 0; i < no_of_vertices; i++)
             {
               newVertices[i].z = (float)(Math.Cos(Math.PI*newVertices[i].x)*
                                          Math.Cos(Math.PI*newVertices[i].y)*
                                          Math.Sin((float)a*t));
             }  
        
         my_mesh.vertices = newVertices;

         my_mesh.RecalculateNormals();
         my_mesh.RecalculateBounds();
         GetComponent<MeshFilter>().mesh = my_mesh;
    } 
}