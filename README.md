# How to Read a PDF File into a String in Python

The Python code main.py uses the Sensible API to extract data from a PDF document. The PDF document is assumed to be of type "tax_forms" or any other name you have used when creating the document type in the Sensible web application. The extracted data from this document will be returned in a JSON format.

The code begins by importing the necessary modules, `json` and `requests`. It then defines three variables: `DOCUMENT_TYPE`, `DOCUMENT_PATH`, `OUTPUT_PATH` , `ERROR_PATH` and `API_KEY`.

To elaborate:

- `DOCUMENT_TYPE` is the type of document to extract data from. In this case, the document type is  "tax_document".
- `DOCUMENT_PATH` specifies the file path to the local PDF document on your computer that you'll extract data from and convert to JSON format. For this example, you'll use the [`1040_2020_sample.pdf`](https://github.com/artem-oppermann/-How-to-Read-a-PDF-File-into-a-String-in-Python/blob/main/2020-TaxReturn.pdf) document.
-`OUTPUT_PATH` is the path where the response will be saved as json file
- `ERROR_PATH` is the path where a possible exception will be saved as json file

- `API_KEY` is your unique Sensible API key, used for authentication.

The script defines a function` api_call()`, which opens the PDF file, reads its contents, and sends a POST request to the Sensible API, with the PDF content and headers included. The `extract_doc()` function then leverages api_call to retrieve the API's response. It verifies the success of the response; in case of an HTTP error, it catches the exception and writes it to a file. In case of a successful response, the function accesses some key-values pairs within the `parsed document` in the response and prints this information. Lastly, the function saves the entire JSON response from the Sensible API into a specified output file. This file can then be used for further analysis or processing of the extracted data.

Finally, the code checks if the script is being run as the main module (`__name__ == '__main__'`), and if it is, it calls the `extract_doc()` function. This ensures that the function is only called when the script is run as a standalone program and not when it's imported as a module.

To run the code, be sure to specify your API key, the local path to your PDF, and the name of the document type that you created in the Sensible web application. You can execute the file either in a console or in an IDE like [Spyder](https://www.spyder-ide.org/) or [PyCharm](https://www.jetbrains.com/pycharm/).

After executing the application, you should receive the following output:

```
Name: Cherry Huston, Sr
Street Address:  104 Easy St
City and Zip-Code:  Gaffney SC 293404461
Social security number:  272-82-4743
```

At the same time, all extracted data from the PDF is saved as a JSON file in the `response.json` file. The output represents the information from the PDF in JSON format. As you can see, using a reference document and setting up the configuration once enables you to extract data from any similar-looking PDF.
