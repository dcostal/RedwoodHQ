using System;
using System.Collections.Generic;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;
using System.Diagnostics;

namespace Test_google
{
    class Test_Script
    {
        public void send_dataTo_Google(Dictionary<string, object> Params)
        {             
            Random number = new Random();
            int random_number = number.Next(10);
            
            //String Test_data = " RedwoodHQ" + random_number;
            
            Process.Start("chrome", @"https://www.google.co.in/search?q=RedwoodHQ");
            SendKeys.SendWait(@"{Enter}");
            
            Thread.Sleep(2000);             
           
            
        }
    }
}