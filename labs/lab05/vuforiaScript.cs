using System;
using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.UI;
using Vuforia;

public class vuforiaScript : MonoBehaviour
{
    // member variables
    public Button my_button;
    private Text my_LogText;
    public Renderer renderer;

    public GameObject my_GameObject;
    public GameObject my_ARCamera;
    public GameObject my_sphere;
    public int dbm_val;


    private AndroidJavaObject my_toastObject;
   
    // Start is called before the first frame update
    void Start()
    {
        my_toastObject  = null;
        my_ARCamera     = GameObject.Find("ARCamera");
        my_sphere       = GameObject.Find("Sphere");

        my_sphere.SetActive(false);

        Button btn      = my_button.GetComponent<Button>();
        my_LogText      = GameObject.Find("LogText").GetComponent<Text>();

        // getting the RSSI value for the network you are connected to
        AndroidJavaObject activity     = new AndroidJavaClass("com.unity3d.player.UnityPlayer").GetStatic<AndroidJavaObject>("currentActivity");
        var wifiManager                = activity.Call<AndroidJavaObject>("getSystemService", "wifi");
        try{
            AndroidJavaObject wifiInfo = wifiManager.Call<AndroidJavaObject>("getConnectionInfo");
            dbm_val                    = wifiInfo.Call<int>("getRssi");
         }
         catch (Exception e) {
             my_LogText.text += "Exception " + e + "\n";
        }
        my_LogText.text = "DBM = " + dbm_val + "\n";

        btn.onClick.AddListener(delegate{ TaskOnClick(btn); } );

        /*AndroidJavaClass toastClass    = new AndroidJavaClass ("android.widget.Toast");
        AndroidJavaClass unityActivity = new AndroidJavaClass ("com.unity3d.player.UnityPlayer");
        object [] toastParams          = new object [3];
        toastParams [0]                = unityActivity.GetStatic<AndroidJavaObject> ("currentActivity");
        toastParams [1]                = "counter = " + m_update_ctr + "\n";
        toastParams [2]                = toastClass.GetStatic<int> ("LENGTH_LONG");
        if (my_toastObject != null) my_toastObject.Call ("cancel");
        my_toastObject                 = toastClass.CallStatic<AndroidJavaObject>("makeText", toastParams);
        my_toastObject.Call("show");
        */
        
    }

    // Update is called once per frame
    void Update()
    {
        
    } 
    
    // task method
    void TaskOnClick(Button btn ) {
        renderer    = my_sphere.GetComponent<Renderer>();

        my_GameObject = Instantiate(my_sphere,  my_ARCamera.transform.position, my_ARCamera.transform.rotation);
        my_GameObject.SetActive(true);

        if (dbm_val < -75) {
            // my_sphere.useGravity    = true;
            renderer.material.color = Color.red;
        }
        else {
            if (dbm_val > -50) {
                // my_sphere.useGravity    = true;
                renderer.material.color = Color.green;
            }
            else {
                // my_sphere.useGravity    = true;
                renderer.material.color = Color.yellow;
            }
        }
        
    }
}
