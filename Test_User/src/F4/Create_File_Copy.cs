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
    class Create_File_Copy
    {
        public string File_Copy()
        {
            String Excel_Path_Text ="C:/repo/Figure4_Web_UI/trunk/Figure4_Web_UI/src/QA/Figure4_Web_Automation/Figure4_Files/abcd testing.PXL";

            //finding the file name from the path and storing only file name in string variable called File_name
            //appending file extension and storing value in Source_File_name
            int occurence = Excel_Path_Text.LastIndexOf("a");
            int length = Excel_Path_Text.IndexOf(".") - occurence;
            String File_Name = Excel_Path_Text.Substring(occurence, length);
            String Source_File_Name = File_Name + ".pxl";
            Console.WriteLine(Source_File_Name + "\n");

            //appending date to file_name and storing in destination_file_name
            String Date = DateTime.Now.ToString("yyyy-MM-dd-HH-mm-ss");
            String Destination_File_Name = File_Name + "-" + Date + ".pxl";
            Console.WriteLine(Destination_File_Name + "\n");

            string sourcePath = @"C:\repo\Figure4_Web_UI\trunk\Figure4_Web_UI\src\QA\Figure4_Web_Automation\Figure4_Files\";
            string targetPath = @"C:\repo\Figure4_Web_UI\trunk\Figure4_Web_UI\src\QA\Figure4_Web_Automation\Figure4_Files\";

            string sourceFile = System.IO.Path.Combine(sourcePath, Source_File_Name);
            //Console.WriteLine(sourceFile);
            string destFile = System.IO.Path.Combine(targetPath, Destination_File_Name);
            //Console.WriteLine(destFile);

            //creating a copy of the file with the name specified
            System.IO.File.Copy(sourceFile, destFile, true);
            //return the new file path
            return (destFile);
            
        }      
        
    }
}