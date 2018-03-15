#This function analyses the data provided by the panel codes
import numpy as np
import matplotlib.pyplot as plt
from os import listdir

def extractMeshConv(angles = (0, 6, 15)):
    from matplotlib.ticker import MultipleLocator
    abspath = "./Panel_code/results/"
    folders = listdir(abspath)
    #here we parse the folder names
    data = {'0deg' : None,'6deg' : None,'15deg' : None}

    xs = (0, 2, 4 ,6 ,8 ,10 ,12 ,14 ,16 ,18, 20, 22 ,24, 26 ,28 ,30 ,32 ,34 ,36 ,38 ,40)
    ys = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19,20)
    X,Y = np.meshgrid(xs,ys)
    for ang in angles:
        dat = {'red' : (X*0)/0,
               'green' : (X*0)/0,
               'yellow' : (X*0)/0}
        for i,x in enumerate(xs):
            for j,y in enumerate(ys):
                for s, sec in enumerate(dat):
                    if str(ang)+'deg_'+str(x)+'x'+str(y) in folders:
                        temp = np.genfromtxt(abspath+str(ang)+'deg_'+str(x)+'x'+str(y)+'/sect_00'+str(s+1),delimiter = (17,17))
                        dat[sec][j,i] = -np.trapz(temp[:,1],x=temp[:,0])
        data[str(ang)+'deg'] = dat
    #plot the graphs
    fig, axs = plt.subplots(nrows = 3, ncols =3, sharex=True,sharey=True)
    del i,j
    clev = np.arange(0,1.5,.01)
    headings = [str(i)+'deg' for i in angles]
    for i,item in enumerate(['red','yellow','green']):
        for j, jtem in enumerate(['0deg','6deg','15deg']):
            ax = axs[i][j]
            #CS = ax.contour(X,Y,data[jtem][item],colors='k')#, levels=[Cls[item][j]],colors = ('w',))
            #ax.clabel(CS, colors = 'w', fontsize=8)
            CSF = ax.contourf(X,Y,data[jtem][item],clev,cmap=plt.cm.plasma)
            ax.set_xlim((0,40))
            ax.set_ylim((0,20))
            ax.xaxis.set_minor_locator(MultipleLocator(2))
            ax.xaxis.set_major_locator(MultipleLocator(10))
            ax.yaxis.set_minor_locator(MultipleLocator(1))
            ax.grid(True,which='both')
    cbar_ax = fig.add_axes([0.85, 0.15, 0.03, 0.80])
    cb =fig.colorbar(CSF,cax=cbar_ax, extend='both')
    cb.ax.set_title('$C_L$')
    #labels
    axs[2][0].set_xlabel('Panels along airfoil\n section 1')
    axs[2][1].set_xlabel('Panels along airfoil\n section 2')
    axs[2][2].set_xlabel('Panels along airfoil\n section 3')
    axs[0][0].set_ylabel('$0^\\circ$\nPanels along span')
    axs[1][0].set_ylabel('$6^\\circ$\nPanels along span')
    axs[2][0].set_ylabel('$15^\\circ$\nPanels along span')
    fig.set_size_inches(7,6)
    fig.subplots_adjust(left=0.1, right=0.8, top =0.99,bottom=0.15)
    #fig.tight_layout()
    #save
    fig.savefig('mesh_convergence.png',dpi =300)
#run the function
extractMeshConv()
plt.show()
