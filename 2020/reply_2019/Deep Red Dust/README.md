# Deep Red Dust

It seems like a ZIP archive, but if we look closer, the header reminds a PNG header (`xxd Deep_Red_Dust | head`). We can reconstruct the header, using `dd`. The header of PNG is `\x89\x50\x4e\x47`. The resulting image contains a string that can be used in the future.

If we use `binwalk` on the file, we will get a ZIP archive, that can be extracted using the password found inside the image.

The file inside the archive is `Goodbye.docm`. `oledump` can help to analyze these files and find interesting streams of data.