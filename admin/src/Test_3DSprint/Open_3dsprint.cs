using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.Threading.Tasks;
using System.Threading;
using System.Diagnostics;

namespace Test_3DSprint{
    class Open_3dsprint{
        public void run(Dictionary<string, object> Params)
        {
            try
     			{
                    Process p = null;
                    if (p == null)
          			{
            			p = new Process();
            			//p.StartInfo.FileName = "3D Sprint Beta.exe";
                        //p.StartInfo.FileName= "C:/Program Files/3D Systems/3D Sprint Beta/3DSprint.exe";
                        p.StartInfo.FileName = "C:/Users/Larissa/Desktop/3dsprint/[0.15.1682]_tp_zipped_selected_file/Mainline_0.15.1682/AutomationScripts/LocalScript/Initiate.bat";
            			p.Start();
                        Thread.Sleep(2000);
                    	p.Close();
          			}
         			else
             			{
                			p.Close();
               	 			p.Dispose();
             			}
         		}
        	catch (Exception e)
            	{
                	Console.WriteLine("Excepton" + e.Message);
            	} 
            
        }
    }
}