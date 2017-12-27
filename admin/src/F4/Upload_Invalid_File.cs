using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Windows.Forms;
using OpenQA.Selenium; 


namespace F4
{
    class Invalid_file_format_upload
    {
        public string run(Dictionary<string, object> Params)
        {
            string sourcePath = @"C:\repo\Figure4_Web_UI\trunk\Figure4_Web_UI\src\QA\Figure4_Web_Automation\Figure4_Files\";
            String Source_File_Name = "Invalid_file_format.txt";
            string sourceFile = System.IO.Path.Combine(sourcePath, Source_File_Name);
            SendKeys.SendWait(sourceFile);
            Thread.Sleep(3000);
            SendKeys.SendWait(@"{Enter}");
            Thread.Sleep(2000); 
            return (sourceFile);
        }
    }
}