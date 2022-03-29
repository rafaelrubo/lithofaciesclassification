//Opening the file
open(".../filename.jpg");

// Running Non-Local Means
run("Non-local Means Denoising", "sigma=15 smoothing_factor=1");
run("Select All");
run("Copy");
newImage("Untitled", "RGB white", 500, 500, 1);
run("Paste");
saveAs("Jpeg", ".../filename_nlm.jpg");
selectWindow("filename.jpg");
close();

// Applying spectral augmentations
selectWindow("filename_nlm.jpg");
run("Duplicate...", "title=filename_nlm_spectral.jpg");

//Histogram equalization
run("Enhance Contrast...", "saturated=0.3 equalize");
saveAs("Jpeg", ".../filename_nlm_spectral01.jpg");
close();
selectWindow("filename_nlm.jpg");
run("Duplicate...", "title=filename_nlm_spectral.jpg");

//Contrast stretching
run("Enhance Contrast...", "saturated=0.3");
saveAs("Jpeg", ".../filename_nlm_spectral02.jpg");
close();
selectWindow("filename_nlm.jpg");
run("Duplicate...", "title=filename_nlm_spectral.jpg");

//Sharpen
run("Sharpen");
saveAs("Jpeg", ".../filename_nlm_spectral03.jpg");
close();
selectWindow("filename_nlm.jpg");
run("Duplicate...", "title=filename_nlm_spectral.jpg");

//Dichromacy deuteranope
run("Dichromacy", "simulate=Deuteranope create");
saveAs("Jpeg", ".../filename_nlm_spectral07.jpg");
close();
selectWindow("filename_nlm.jpg");

//Dichromacy tritanope
run("Dichromacy", "simulate=Tritanope create");
saveAs("Jpeg", ".../filename_nlm_spectral08.jpg");
close();
selectWindow("filename_nlm_spectral.jpg");

//Red color casting
run("Split Channels");
selectWindow("filename_nlm_spectral.jpg (blue)");
run("Enhance Contrast...", "saturated=0.3");
selectWindow("filename_nlm_spectral.jpg (green)");
run("Enhance Contrast...", "saturated=0.3");
run("Merge Channels...", "c1=[filename_nlm_spectral.jpg (red)] c2=[filename_nlm_spectral.jpg (green)] c3=[filename_nlm_spectral.jpg (blue)] create");
run("Stack to RGB");
saveAs("Jpeg", ".../filename_nlm_spectral04.jpg");
close();
selectWindow("Composite");
close();
selectWindow("filename_nlm.jpg");
run("Duplicate...", "title=filename_nlm_spectral.jpg");

//Green color casting
run("Split Channels");
selectWindow("filename_nlm_spectral.jpg (red)");
run("Enhance Contrast...", "saturated=0.3");
selectWindow("filename_nlm_spectral.jpg (blue)");
run("Enhance Contrast...", "saturated=0.3");
run("Merge Channels...", "c1=[filename_nlm_spectral.jpg (red)] c2=[filename_nlm_spectral.jpg (green)] c3=[filename_nlm_spectral.jpg (blue)] create");
run("Stack to RGB");
saveAs("Jpeg", ".../filename_nlm_spectral05.jpg");
close();
selectWindow("Composite");
close();
selectWindow("filename_nlm.jpg");
run("Duplicate...", "title=filename_nlm_spectral.jpg");

//Blue color casting
run("Split Channels");
selectWindow("filename_nlm_spectral.jpg (green)");
run("Enhance Contrast...", "saturated=0.3");
selectWindow("filename_nlm_spectral.jpg (red)");
run("Enhance Contrast...", "saturated=0.3");
run("Merge Channels...", "c1=[filename_nlm_spectral.jpg (red)] c2=[filename_nlm_spectral.jpg (green)] c3=[filename_nlm_spectral.jpg (blue)] create");
run("Stack to RGB");
saveAs("Jpeg", ".../filename_nlm_spectral06.jpg");
close();
selectWindow("Composite");
close();
selectWindow("filename_nlm.jpg");
run("Duplicate...", "title=filename_nlm_spectral.jpg");

//vignette
run("Split Channels");
selectWindow("filename_nlm.jpg");
close();
run("Images to Stack", "name=Stack title=[] use");
run("BaSiC ", "processing_stack=Stack flat-field=None dark-field=None shading_estimation=[Skip estimation and use predefined shading profiles] shading_model=[Estimate flat-field only (ignore dark-field)] setting_regularisationparametes=Automatic temporal_drift=Ignore correction_options=[Compute shading and correct images] lambda_flat=0.50 lambda_dark=0.50");
selectWindow("Flat-field:Stack");
selectWindow("Corrected:Stack");
run("Stack to Images");
run("Merge Channels...", "c1=[filename_nlm_spectral.jpg (red)] c2=[filename_nlm_spectral.jpg (green)] c3=[filename_nlm_spectral.jpg (blue)] create");
run("Stack to RGB");
saveAs("Jpeg", ".../filename_nlm_spectral09.jpg");
close();
close();
close();
close();