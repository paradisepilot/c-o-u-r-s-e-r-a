% This script contains the solutions for the code for some simple examples.
% There is also a call to each of the functions that you should create that
% is commented out.  WHEN YOU HAVE FINISHED WRITING A FUNCTION, COMMENT OUT 
% THE SOLUTION, UNCOMMENT THE CALL TO YOUR CODE, AND USE THIS SCRIPT TO 
% TO TEST YOUR FUNCTION.  Check that this script runs to completion and 
% that your answer matches the solution.  Once your function seems to be
% working, submit it for the unit test.

% Testing phenotypeGivenGenotypeMendelianFactor:
isDominant = 1;
genotypeVar = 1;
phenotypeVar = 3;
phenotypeFactor         = struct('var', [3,1], 'card', [2,3], 'val', [1,0,1,0,0,1]); % Comment out this line for testing
computedPhenotypeFactor = phenotypeGivenGenotypeMendelianFactor(isDominant, genotypeVar, phenotypeVar);

%disp("phenotypeFactor");
%disp( phenotypeFactor );
%disp("computedPhenotypeFactor");
%disp( computedPhenotypeFactor );

% Testing phenotypeGivenGenotypeFactor:
alphaList = [0.8; 0.6; 0.1];
genotypeVar = 1;
phenotypeVar = 3;
phenotypeFactorAlpha = struct('var', [3,1], 'card', [2,3], 'val', [0.8,0.2,0.6,0.4,0.1,0.9]); % Comment out this line for testing
computedPhenotypeFactorAlpha = phenotypeGivenGenotypeFactor(alphaList, genotypeVar, phenotypeVar);

%disp("phenotypeFactorAlpha");
%disp( phenotypeFactorAlpha );
%disp("computedPhenotypeFactorAlpha");
%disp( computedPhenotypeFactorAlpha );

% Testing genotypeGivenAlleleFreqsFactor:
alleleFreqs = [0.1; 0.9];
genotypeVar = 1;
genotypeFactor         = struct('var', [1], 'card', [3], 'val', [0.01,0.18,0.81]); % Comment out this line for testing
computedGenotypeFactor = genotypeGivenAlleleFreqsFactor(alleleFreqs, genotypeVar);

%disp("genotypeFactor");
%disp( genotypeFactor );
%disp("computedGenotypeFactor");
%disp( computedGenotypeFactor );

%alleleFreqs = [0.1; 0.3; 0.6];
%temp = genotypeGivenAlleleFreqsFactor(alleleFreqs, genotypeVar);
%disp("temp");
%disp( temp );
%disp("sum(temp.val)");
%disp( sum(temp.val) );

% Testing genotypeGivenParentsGenotypesFactor:
numAlleles = 2;
genotypeVarChild = 3;
genotypeVarParentOne = 1;
genotypeVarParentTwo = 2;
genotypeFactorPar         = struct('var', [3,1,2], 'card', [3,3,3], 'val', [1,0,0,0.5,0.5,0,0,1,0,0.5,0.5,0,0.25,0.5,0.25,0,0.5,0.5,0,1,0,0,0.5,0.5,0,0,1]);
computedGenotypeFactorPar = genotypeGivenParentsGenotypesFactor(numAlleles, genotypeVarChild, genotypeVarParentOne, genotypeVarParentTwo);

%disp("genotypeFactorPar");
%disp( genotypeFactorPar );
%disp("computedGenotypeFactorPar");
%disp( computedGenotypeFactorPar );
%disp("transpose([genotypeFactorPar.val, computedGenotypeFactorPar.val])");
%disp( transpose([genotypeFactorPar.val; computedGenotypeFactorPar.val]) );
%disp("TEMP");
%disp( transpose([transpose(IndexToAssignment(1:length(genotypeFactorPar.val),genotypeFactorPar.card)); genotypeFactorPar.val; computedGenotypeFactorPar.val]) );

%TEMP = abs(genotypeFactorPar.val - computedGenotypeFactorPar.val);
%disp("TEMP");
%disp( TEMP );
%disp("sum(TEMP)");
%disp( sum(TEMP) );

% Testing constructGeneticNetwork:
pedigree = struct('parents', [0,0;1,3;0,0]);
pedigree.names = {'Ira','James','Robin'};
alleleFreqs = [0.1; 0.9];
alphaList = [0.8; 0.6; 0.1];
%sampleFactorList         = load('sampleFactorList.mat'); % Comment out this line for testing
load('sampleFactorList.mat'); % Comment out this line for testing
computedSampleFactorList = constructGeneticNetwork(pedigree, alleleFreqs, alphaList);

%disp("########################################");
%disp("sampleFactorList");
%disp( sampleFactorList );
%disp("computedSampleFactorList");
%disp( computedSampleFactorList );
%disp("########################################");
%disp("sampleFactorList.sampleFactorList(1)");
%disp( sampleFactorList.sampleFactorList(1) );
%disp("computedSampleFactorList(1)");
%disp( computedSampleFactorList(1) );
%disp("########################################");
%disp("sampleFactorList.sampleFactorList(2)");
%disp( sampleFactorList.sampleFactorList(2) );
%disp("computedSampleFactorList(2)");
%disp( computedSampleFactorList(2) );
%disp("########################################");
%disp("sampleFactorList.sampleFactorList(3)");
%disp( sampleFactorList.sampleFactorList(3) );
%disp("computedSampleFactorList(3)");
%disp( computedSampleFactorList(3) );
%disp("########################################");
%disp("sampleFactorList.sampleFactorList(4)");
%disp( sampleFactorList.sampleFactorList(4) );
%disp("computedSampleFactorList(4)");
%disp( computedSampleFactorList(4) );
%disp("########################################");
%disp("sampleFactorList.sampleFactorList(5)");
%disp( sampleFactorList.sampleFactorList(5) );
%disp("computedSampleFactorList(5)");
%disp( computedSampleFactorList(5) );
%disp("########################################");
%disp("sampleFactorList.sampleFactorList(6)");
%disp( sampleFactorList.sampleFactorList(6) );
%disp("computedSampleFactorList(6)");
%disp( computedSampleFactorList(6) );
%disp("########################################");

% Testing phenotypeGivenCopiesFactor:
alphaListThree = [0.8; 0.6; 0.1; 0.5; 0.05; 0.01];
numAllelesThree = 3;
genotypeVarMotherCopy = 1;
genotypeVarFatherCopy = 2;
phenotypeVar = 3;
phenotypeFactorPar         = struct('var', [3,1,2], 'card', [2,3,3], 'val', [0.8,0.2,0.6,0.4,0.1,0.9,0.6,0.4,0.5,0.5,0.05,0.95,0.1,0.9,0.05,0.95,0.01,0.99]);
computedPhenotypeFactorPar = phenotypeGivenCopiesFactor(alphaListThree, numAllelesThree, genotypeVarMotherCopy, genotypeVarFatherCopy, phenotypeVar);

disp("length(phenotypeFactorPar.val)");
disp( length(phenotypeFactorPar.val) );

%disp("phenotypeFactorPar");
%disp( phenotypeFactorPar );
%disp("computedPhenotypeFactorPar");
%disp( computedPhenotypeFactorPar );
%disp("sum(abs(phenotypeFactorPar.val - computedPhenotypeFactorPar.val))");
%disp( sum(abs(phenotypeFactorPar.val - computedPhenotypeFactorPar.val)) );

% Testing constructDecoupledGeneticNetwork:
pedigree = struct('parents', [0,0;1,3;0,0]);
pedigree.names = {'Ira','James','Robin'};
alleleFreqsThree = [0.1; 0.7; 0.2];
alleleListThree = {'F', 'f', 'n'};
alphaListThree = [0.8; 0.6; 0.1; 0.5; 0.05; 0.01];
load('sampleFactorListDecoupled.mat');
computedSampleFactorListDecoupled = constructDecoupledGeneticNetwork(pedigree, alleleFreqsThree, alphaListThree);

for i = 1:length(sampleFactorListDecoupled)
	disp("########################################");
	%disp(strcat("sampleFactorListDecoupled(",int2str(i),")"));
	%disp( sampleFactorListDecoupled(i) );
	disp(strcat("computedSampleFactorListDecoupled(",int2str(i),")"));
	disp( computedSampleFactorListDecoupled(i) );
	%disp("sum(abs(sampleFactorListDecoupled(i).val - computedSampleFactorListDecoupled(i).val ))");
	%disp( sum(abs(sampleFactorListDecoupled(i).val - computedSampleFactorListDecoupled(i).val )) );
end

% Testing constructSigmoidPhenotypeFactor:
alleleWeights = {[3, -3], [0.9, -0.8]};
geneCopyVarParentOneList = [1; 2];
geneCopyVarParentTwoList = [4; 5];
phenotypeVar = 3;
phenotypeFactorSigmoid = struct('var', [3,1,2,4,5], 'card', [2,2,2,2,2], 'val', [0.999590432835014,0.000409567164986080,0.858148935099512,0.141851064900488,0.997762151478724,0.00223784852127629,0.524979187478940,0.475020812521060,0.858148935099512,0.141851064900488,0.0147740316932731,0.985225968306727,0.524979187478940,0.475020812521060,0.00273196076301106,0.997268039236989,0.997762151478724,0.00223784852127629,0.524979187478940,0.475020812521060,0.987871565015726,0.0121284349842742,0.167981614866076,0.832018385133925,0.524979187478940,0.475020812521060,0.00273196076301106,0.997268039236989,0.167981614866076,0.832018385133925,0.000500201107079564,0.999499798892920]);  % Comment out this line for testing
computedPhenotypeFactorSigmoid = constructSigmoidPhenotypeFactor(alleleWeights, geneCopyVarParentOneList, geneCopyVarParentTwoList, phenotypeVar);

%disp("phenotypeFactorSigmoid");
%disp( phenotypeFactorSigmoid );
%disp("computedPhenotypeFactorSigmoid");
%disp( computedPhenotypeFactorSigmoid );
%disp("sum(abs(phenotypeFactorSigmoid.val - computedPhenotypeFactorSigmoid.val))");
%disp( sum(abs(phenotypeFactorSigmoid.val - computedPhenotypeFactorSigmoid.val)) );

