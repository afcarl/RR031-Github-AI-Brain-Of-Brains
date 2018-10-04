
GITHUB AI Brain-of-Brains:

Demo Website: https://www.2strikehitter.com/AI_BrainofBrains.html

Overview of Github Repo "AI-Brain-of-Brains" Video: https://youtu.be/aCSP6noa2_M

Overview of AI Brain #1: "Github-Repos-by-Title" Video: https://youtu.be/jVd5xPxyeYA

Overview of AI Brain #2: "Github-Repos-by-Author" Video: https://youtu.be/yxWlqWwlms8

Overview of AI Brain #3: "Github-Repos-by-Tags" Video: https://youtu.be/Tldj3fW8yrE

Overview of AI Brain #4: "Github-Repos-by-Most-Similar-Repos" Video: https://youtu.be/FWYPav2pK2g

Overview of AI Brain #5: "Github-Repos-by-Most-Similar-Repos-Tags" Video: https://youtu.be/7KiTZgHX3kU


"GITHUB AI Brain-of-Brains" is a WIP. It's intended purpose is to act as a personal productivity tool to provide more effective heretofore Github Repo search capability with both visual feedback as to repos with specific TAGS, and a visual and quantitative indication of similar natured repros. As you are aware, the state of Github repo documentation varies from "none" to "extensive". As such, it is a bit of an evolving art to capture sufficient input for Gensim/DOC2VEC to make meaningful generaliations as to "Similar" and "DisSimilar" repo determinations. A toy data set of (1000) Github repos is provided located in "https://github.com/afcarl/GITHUB2VEC/1_Repo_data/github.com/afcarl/Github_Repo_html_txt_files_1000.zip".


*****************************************************
START: Example of "GITHUB AI Brain-of-Brains" Output:
*****************************************************
GITHUB REPRO NAME: "ABC-GAN"

REPRO AUTHOR: "IGORSUSMELJ"

REPO TAGS: ['IMAGE', 'BLUR', 'LSUN', 'CONTROLLER', 'GAN']

MOST SIMILAR REPOS ArgMin(10,Score>0.5): [('ABC-GAN', 1.0), ('BICYCLEGAN-PYTORCH', 0.6996548175811768), ('6853-PROJECT', 0.6616806983947754), ('BICYCLEGAN-TENSORFLOW', 0.5852857828140259), ('ANIMEGAN', 0.5558176040649414), ('AC-GAN', 0.551661491394043), ('BAYESGAN', 0.5287083387374878), ('AGE', 0.5171400308609009)]

MOST SIMILAR REPOS TAGS: ['IMAGE', 'GAN', 'TRAIN', 'DATA', 'DATASET']

MOST DISSIMILAR REPOS ArgMin(10,Score<0.05): [('AWS-BIG-DATA-BLOG', 0.00018744543194770813), ('ARISTO-MINI', 0.00030460208654403687), ('A_COURSE_IN_TIMESERIES', 0.00031220726668834686), ('AIS_DEMO', 0.0003952424740418792), ('ADT_OPT', 0.0004009399563074112), ('BAYESIAN-KALMANFILTER', 0.0004142019897699356), ('AWESOME-AWESOME-AWESOME', 0.00048428773880004883), ('BAYES', 0.0006488114595413208), ('ARXIV-TOPICS', 0.0006780996918678284), ('2013_FALL_ASTR599', 0.0006959773600101471)]

MOST DISSIMILAR REPOS TAGS: ['AWS', 'BLOG', 'DATA']
*****************************************************
END: Example of "GITHUB AI Brain-of-Brains" Output:
*****************************************************


1. Pre-Requisits:

1a. GITHUB2VEC: https://github.com/afcarl/GITHUB2VEC

1b. "The Brain" software: https://www.thebrain.com/

2. Create your Github Repo collection (or use the provided toy dataset of (1000) Github Repos).

3. Using "GITHUB2VEC", create the input files for "AI-Brain-of-Brains"

4. From inside "The Brain" software, Create a new "Brain" named "BRAIN01".
5. From inside "The Brain" software, Rename the single node "ROOT"
6. From inside "The Brain" software, Create a "Brain" archive: "File"/"Backup to Brain Archive"/"Backup"
7. Copy the ".brz" file to the "./0_REF" folder.
8. Rename the ".brz" file to ".zip".
9. Extract the ".zip" file to the "./0_REF" folder.

10. Create "Brain #1", "Github-Repos-by-Title", by running: "BRAIN9_Archive_IO_BRAIN01_TITLES_t1.py". Output is written to the "./results" folder.
10a. Input #1: "output_081918_1000.dat"
10b. Input #2: "doc_title_Similar_dict_1000.zpkl"
10c. Input #3: "doc_title_Similar_TAGS_dict_1000.zpkl"
10d. Input #4: "doc_title_Similar_TAGS_dict_all_1000.zpkl"
10e. Input #5: "doc_title_DisSimilar_dict_1000.zpkl"
10f. Input #6: "doc_title_DisSimilar_TAGS_dict_1000.zpkl"
10g. Input #7: "doc_title_DisSimilar_TAGS_dict_all_1000.zpkl"
10h. Input #8: "forked_author_dict_1000.zpkl"
10j. Input #9: "forked_author_to_titles_dict_1000.zpkl"

11. From the "./results" folder, add the entire contents to a zip file "results.zip".
12. Rename the zip file "results.zip" to "results.brz".
13. From inside "The Brain" software, delete both the local copy of the "BRAIN01" brain.
14. From inside "The Brain" software, import the new "BRAIN01" brain (i.e. "results.brz"): "File"/"Import"/"Brain Archive (brz)"

15. Repeat Steps #4 through #14, for "BRAIN02", by running: "BRAIN9_Archive_IO_BRAIN02_AUTHOR_u.py".

16. Repeat Steps #4 through #14, for "BRAIN03", by running: "BRAIN9_Archive_IO_BRAIN03_TAGS_s1.py".

17. Repeat Steps #4 through #14, for "BRAIN04", by running: "BRAIN9_Archive_IO_BRAIN04_SIMILAR_v.py".

18. Repeat Steps #4 through #14, for "BRAIN05", by running: "BRAIN9_Archive_IO_BRAIN05_SIMILARTAGS_w.py".










