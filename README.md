# Practical-modelling

Generate the 3D structure of the α-amylase protein

Step1: Identification and Selection of Template structure

 1.Get access to Uniprot database  (http://www.uniprot. org/) to get the protein sequence of AA     (Target Sequence)
 PDB code: 1AQM

 2.Download the sequence in fasta format

 3.Elimination of the initiating sequence 
 Tool used:  Signa lP - 6.0

 4.Searching  for template  : homologous protein to the target sequence 
 
 Tool used: Basic Local Alignment Search Tool (BLAST)
 in this case we use Blast to identify sequences in different species that are similar or homologous to our target sequence 
 Parameters used:
 Databases: Standard databases 
 Database : Protein Data Bank proteins (pdb)
 Algorithm: blastp (protein-protein BLAST)

 5.Template sequence selection 
 
 various factors are considered in choosing an eligible template:
 
 Sequence similarity level of the template sequence in relative to the target sequence :  >25% , this will increase the accuracy of the model          being generated 
 
 Sequence identity level: is defined as the percentage of residues of the two aligned proteins that are identical, there are three levels by    which sequence identity can be categorized: low, intermediate and high levels of sequence identity. However, the intermediate levels of sequence     identity,  between the two aligned proteins is 25% 90%.
 
 Query Coverage: refers to the fraction of a query sequence that is aligned to a database sequence in a sequence alignment. It represents the   percentage of the query sequence that is covered by the alignment with the database sequence. A higher query cover indicates a more complete   alignment between the query and database sequences.
 
 E-Value: the number of alignments expected by chance with the calculated score or better. The expect value is the default sorting metric; for  significant alignments the E value should be very close to zero.
 
Template quality:  the template should  has been experimentally determined and has a high resolution, resolution should be between 1A to 3A.

 Conserved regions: choose the template with conserved regions  that align well with the target protein sequence. This will help ensure that the  model accurately captures the structural features of the protein
 
Phylogenetic similarity between template and target sequences

Environmental factors such as pH, solvent type and existence of bound ligand…

 The template was chosen based on the prameters mentioned before
 PDB code: 1KXQ
 
 characteristic of the chosen template:
    E-value: 1e -135
    Coverage: 66%
    Identity: 47.24%
    resolution: 1.6A
    Organism: Sus scrofa (pig) Eukaryota

 6.Download the template sequence in fasta format

Step 2: Pairwise alignment between the target and the template sequences 

 Tool used: EMBOSS Needle
 
 Pairwise alignment is done in order to determine the level of similarity between the two sequences, by aligning the sequences, we can identify  regions of high sequence identity and similarity, which can indicate conserved structural elements and functional domains. This information can then be used to guide the modeling of the target protein's 3D structure based on the template structure.
 pairwise alignment can help identify potential errors or gaps in the alignment, which may need to be addressed to improve the accuracy of the   predicted 3D structure.

Step 3: Building the homology model

 Tool used :Modeller
 
 1.Download the 3D structure of the template sequence from PDB
 
 2.Creating the input file: 

 PDB file for 3D structures of the template: water molecules are manually removed
 
Script :

 
    PDB file for 3D structures of the template: water molecules are manually removed
    Script 
    from modeller import *
    from modeller.automodel import *

    env = environ()
    env.io.pdb_files_directory = ['C:\\Users\\Skymil\\Desktop\\atom_files\\1KXQ_A.pdb']
    knowns = '1KXQ_A'
    sequence = 'sp_P29957_AMY_PSEHA'

    a = AutoModel(env,
    alnfile='alig.pir', 
    knowns=knowns,
    sequence=sequence,
    assess_methods=[assess.DOPE,
                  assess.GA341])
                  
    a.starting_model = 1
    a.ending_model = 10

    a.make()
    print("Modeling completed!")

 Alignment file: pir format
 
 The fasta file alignment extension is converted to the pir extension manually
 
 Execute the script by using the command mod 10.5 script name.py


3.Out put of the modeller :

34 elements : Available in the file 'Output modeller'

Step 4 :Quality assessment of the homology model

 1.Selection of the best model:
 
 The selection is made according to the DOPE and GA341 scores
 
 Lowest DOPE score: -53639.77734
 Highest GA341 score: 1
 
 2.Evaluation of the model's quality
 
 1st  tool :Ramachandran plots  to check the stereochemical quality
 
 Phi (φ) and Psi (ψ) Angles: These angles represent the rotation around specific bonds in the protein backbone. 
 The Ramachandran plot depicts the allowed regions for these angles, which correspond to sterically unhindered and energetically stable protein   conformations.
 
 3.MolProbity Results: Available in the file 'Practical modeling.pptx'

 Overall Analysis:

 While the Ramachandran plot analysis suggests a good quality structure (with over 93% of residues in allowed regions and low outlier   percentages ), the presence of C-Beta deviations, bad bonds, and bad angles indicates some potential issues that could be addressed to improve  the overall quality of the structure.
 
 2nd tool : Prosa to check the local quality of the model
 
 Prosa Results: Available in the file 'Practical modeling.pptx'
 
 This plot of local model quality, shows the energy of each amino acid residue in the protein chain is plotted along the x-axis according to its  position (i) in the sequence.
 Lower energy scores typically indicate more favorable and stable conformations for the residue.
 Higher scores suggest less favorable interactions or potential strain.
 Window size refers to the number of amino acids that are considered together when calculating the local model quality. The smoother the curve,   the better the local model quality is predicted to be.

 Step 5: Alignment of the 3D model selected  with the experimentally solved structure (1AQM)
 
 Tool used: Pymol (to compare two structures)
 Method : Root Mean Square Deviation (RMSD)
 The results and interpretation are available in the file 'Practical modeling.pptx'
 The alignment results suggest a good match between the 3D model and the experimentally solved structure. The high score and low RMSD values  indicate a high degree of similarity between the two structures. 
 This shows how accurate it is the theoretical structure compared to the experimentally determined structure, this can solve the problem of the  gap between the number of discovered sequences and the number of 
 3D structures.
 
 Adopting the theoretical method can save time, money, and produce high quality results.

 Step 6: Alignment of the  template (1KXQ) with the experimentally solved structure (1AQM)

 Pymol results:  The results and interpretation are available in the file 'Practical modeling.pptx'
 
 The result of align shows that the two protein structures are very similar,  with a high MatchAlign score and a low RMSD value


The question that arises is why the model, template, and crystallographic structure are so closely correlated, even though they come from two completely different species ?
Temlate  from Sus scrofa (mammal)
Crystallo  structure from Alteromonas haloplanktis (bacteria) 

The answer to this question will be based on two concepts:

Evolutionary Conservation: even though pigs and bacteria are distantly related organisms, some proteins may share similar structures and functions because they evolved from a common ancestor but diverging significantly over time. 
These conserved proteins might play essential roles in basic biological processes that are necessary for all life forms. 

Convergent Evolution :  the proteins might have evolved independently to perform similar functions and converged on similar structures despite having different sequences.

Based on the two concepts, it is possible to suggest that this protein structure (α-amylase ) is likely crucial for its function and has been conserved throughout evolution or has converged due to functional pressure.

In summary, the high degree of consistency between structures from completely different species can be contributed to the power of structural conservation and convergence in protein evolution.



=======
Work details are available in the practical modeling.ppt file
>>>>>>> b1b59ffb0213c79fa891b3a7abfec44bc7468979


