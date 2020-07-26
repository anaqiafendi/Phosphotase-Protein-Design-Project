% Load and clean data
opts = detectImportOptions(fullfile('Processed Data', 'activations.csv'));
opts.VariableNamesLine = 1;
opts.RowNamesColumn = 1;
T = readtable(fullfile('Processed Data', 'activations.csv'), opts);
T = removevars(T,{'Var1'});
T([1],:) = [];

% Plot data
mat = table2array(T);
r = 1:size(mat,1);
c = 1:size(mat,2);

figure(1)
mesh(c,r,mat)
grid on
xlabel('Protein ID')
ylabel('Substrate number')
zlabel('Activations')
view(45, 65)