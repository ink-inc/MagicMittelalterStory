import numpy as np
import matplotlib.pyplot as plt

"""
fixed parameters:
mean menopause age: 45, variance: 2
death age variance: 4
mean young child death age: 9, variance: 3
marriage age variance: 1
"""
meno_mean = 45
meno_std = 2
death_std = 6
young_mean = 3
marry_std = 1
next_std = 1

class Family():
    
    def __init__(self, wealth, sim_year):
        self.wealth = wealth
        self.sim_year = sim_year

        pre0 = {"m_marry":17,       #mean marriage age
                "m_death":58,       #mean death age
                "m_child":2.1,      #mean number of children (not to scale)
                "prod":16,          #fertility scaling factor
                "r_embryo":0.12,    #embryo death probability
                "r_mother1":0.07,   #mother death prob at first birth
                "r_mother2":0.035,  #mother death prob at later birth
                "r_death1":0.14,    #child death prob in first year
                "r_death2":0.09,    #child death prob in second year
                "r_death3":0.25}    #child death prob in young age
        pre1 = {"m_marry":20,
                "m_death":63,
                "m_child":1.8,
                "prod":11,
                "r_embryo":0.1,
                "r_mother1":0.06,
                "r_mother2":0.03,
                "r_death1":0.12,
                "r_death2":0.08,
                "r_death3":0.2}
        pre2 = {"m_marry":15,
                "m_death":66,
                "m_child":1.5,
                "prod":6,
                "r_embryo":0.09,
                "r_mother1":0.055,
                "r_mother2":0.02,
                "r_death1":0.1,
                "r_death2":0.07,
                "r_death3":0.15}
        presets = {0: pre0, 1: pre1, 2: pre2} #poor, common, wealthy
        self.p = presets[wealth]
        self.p["r_death2"] /= (1-self.p["r_death1"])
        self.p["r_death3"] /= (1-self.p["r_death1"])*(1-self.p["r_death2"])
        
        self.natural_ages_mother()
        self.conceptions()
        self.child_youths()
        
    def natural_ages_mother(self):
        self.marry = int(np.random.normal(self.p["m_marry"],marry_std)) #marriage age
        self.meno = int(np.random.normal(meno_mean,meno_std))           #menopause age
        self.birth = self.sim_year-self.marry-np.random.randint(0, self.meno//2) #birth year with randomized start
        self.death = int(np.random.normal(self.p["m_death"],death_std))          #natural death age
        self.natural_death = self.death
        self.age = self.marry
    
    def conceptions(self):
        self.conc = []
        first = True
        while self.age<min(self.death,self.meno):
            p = (1.07-0.005*len(self.conc))/(1.07-0.005*len(self.conc)+1)
            sex = np.random.choice([0,1],p=[p,1-p])
            if np.random.rand()<self.p["r_embryo"]*(1+0.02*sex):
                #save year of birth, born/died, mother age at birth, sex
                self.conc.append([self.birth+self.age, "died as embryo", self.age, sex])
            else:
                if first:
                    first = False
                    if np.random.rand()<self.p["r_mother1"]:
                        self.death = self.age
                else:
                    if np.random.rand()<self.p["r_mother2"]:
                        self.death = self.age
                self.conc.append([self.birth+self.age, "born", self.age, sex])
            next_arg = 2*self.p["m_child"]*(1+len(self.conc)**2/self.p["prod"]**2)
            next = round(next_arg+np.random.lognormal(np.log(next_arg*np.exp(-next_std**2/2)), next_std))/2
            self.age += next
        
    def child_youths(self):
        self.children = []
        for c in self.conc:
            if "born" in c[1]:
                if np.random.rand()<self.p["r_death1"]*(1.03-0.03*c[3]):
                    self.children.append([int(c[0])+1, "died at age {} (in year {})".format(1, int(c[0])+1)])
                elif np.random.rand()<self.p["r_death2"]*(1.03-0.03*c[3]):
                    self.children.append([int(c[0])+2, "died at age {} (in year {})".format(2, int(c[0])+2)])
                elif np.random.rand()<self.p["r_death3"]*(1.01-0.01*c[3]):
                    death_age = 3+int(np.random.exponential(young_mean))
                    self.children.append([int(c[0])+death_age, "died at age {} (in year {})".format(death_age, int(c[0])+death_age)])
                else:
                    death_age = int(np.random.normal(self.p["m_death"],death_std))
                    self.children.append([int(c[0])+death_age,"survived! (dies naturally at age {} in year {})".format(death_age,int(c[0])+death_age)])
            else:
                self.children.append([int(c[0]),"died as embryo (in year {})".format(int(c[0]))])
    
    def return_data(self):
        mother_nums = [self.birth, self.marry, self.meno, self.death]
        mother_string = "\tbirth year: {}\n\tmarry age: {} (year {})\n\tmenopause age: {} (year {})\n\tdeath age: {} (year {}, {})".format(mother_nums[0], mother_nums[1], mother_nums[0]+mother_nums[1], mother_nums[2], mother_nums[0]+mother_nums[2], mother_nums[3], mother_nums[3]+mother_nums[0], ["natural", "from birth"][mother_nums[3]<self.natural_death])
        children_string = "\n".join(["\tChild {}:\n\t\tbirth year: {} (mother age: {})\n\t\tsex: {}\n\t\t".format(i+1,c2[0],c2[2],["male","female"][c2[3]])+c[1] for i, [c,c2] in enumerate(zip(self.children,self.conc))])
        return mother_string, children_string
        
    def print_data(self):
        s1,s2 = self.return_data()
        print(s1)
        print(s2)
        
    def calculate_stats(self):
        child_birth = np.sum(["born" in c[1] for c in self.conc])
        child_surv = np.sum(["survived" in c[1] for c in self.children])
        child_conc = len(self.conc)
        female_conc = np.sum([c[3] for c in self.conc])
        male_conc = child_conc-female_conc
        female_birth = np.sum([c[3] and "born" in c[1] for c in self.conc])
        male_birth = child_birth-female_birth
        female_surv = np.sum([c[3] and "survived" in c2[1] for c, c2 in zip(self.conc, self.children)])
        male_surv = child_surv-female_surv
        natural = self.death>=self.natural_death
        return child_conc, child_birth, child_surv, female_conc, female_birth, female_surv, male_conc, male_birth, male_surv, natural
    
    def alive(self, t):
        tmp = [int(c[0])<=t and c2[0]>=t and "embryo" not in c2[1] for c,c2 in zip(self.conc,self.children)]
        tmp.append(self.birth<=t and self.death+self.birth>=t)
        return tmp

def generate_families(num, wealth=1, sim_year=493):
    families = np.empty(num, dtype=object)
    for i in range(num):
        families[i] = Family(wealth, sim_year)
    return families
    
def print_full(families):
    if len(families)>10: families=families[:10]
    for i,f in enumerate(families):
        print("Mother {}".format(i+1))
        f.print_data()

def plot_one_window(families, tmin, tmax, m):
    times = np.arange(tmin,tmax+1)
    num = len(families)
    plt.subplots(min([3,num]),max([1,num//3]))
    plt.tight_layout()
    for i,f in enumerate(families):
        alives = np.asarray([f.alive(t) for t in times]).T
        alives = np.insert(alives[:-1],0,alives[-1],axis=0)
        sexes = [c[3] for c in f.conc]
        sexes.insert(0,1)
        ax = plt.subplot(min([3,num]),max([1,num//3]),i+1)
        plt.title("Family {}".format(i+1+m*6))
        for n,c in enumerate(f.children):
            if "embryo" in c[1] and tmin<=c[0]<=tmax:
                ax.plot([c[0]], [n+1], ["xb","xr"][sexes[n+1]], markersize=10)
        for k,a in enumerate(alives):
            ax.plot(times[a],np.ones_like(times)[a]*k, ["b", "r"][sexes[k]],linewidth=10)
        plt.vlines([485,493],-0.5,len(alives)-0.5,color="g")
        plt.vlines(np.arange((tmin//5)*5,(tmax//5+1)*5+1,5),-0.5,len(alives)-0.5,color="k",linestyles=":")
        ax.set_xticks(list(ax.get_xticks())+[485,493],minor=False)
        ax.set_xticks(times,minor=True)
        ax.set_yticks(np.arange(len(alives)))
        ax.xaxis.grid(which="minor",ls=":")
        ax.yaxis.grid(ls=":")
        plt.ylabel("mother (0) and children numbers")
        plt.xlabel("year")
        plt.xlim(tmin,tmax)
        plt.ylim(-0.5,len(alives)-0.5)
    for i in range((-num)%3):
        ax = plt.subplot(min([3,num]),max([1,num//3]),i+1+num%3+3*(num//3))
        ax.axis("off")
        
def plot_time_line(families, tmin, tmax):
    num = len(families)
    if num>30: families=families[:30]
    if num>6:
        sub_fams = np.split(families, np.arange(1,num//6+(num%6!=0))*6)
        for m, s in enumerate(sub_fams):
            plot_one_window(s, tmin, tmax, m)
    else:
        plot_one_window(families, tmin, tmax, 0)
    plt.show()

def print_stats(families, plots=True):
    num = len(families)
    stats = []
    death_ages = []
    mother_deaths = []
    for f in families:
        stats.append(f.calculate_stats())
        mother_deaths.append(f.death)
        for c,c2 in zip(f.children,f.conc): death_ages.append(c[0]-int(c2[0]))
    child_conc, child_birth, child_surv, female_conc, female_birth, female_surv, male_conc, male_birth, male_surv, natural = np.asarray(stats).T
    tot_conc = np.sum(child_conc)
    tot_birth = np.sum(child_birth)
    tot_surv = np.sum(child_surv)
    tot_f_conc = np.sum(female_conc)
    tot_f_birth = np.sum(female_birth)
    tot_f_surv = np.sum(female_surv)
    tot_m_conc = tot_conc-tot_f_conc
    tot_m_birth = tot_birth-tot_f_birth
    tot_m_surv = tot_surv-tot_f_surv
    tot_natural = np.sum(natural)
    print("Statistics for the Families:")
    print("\tChild conceptions: {}".format(tot_conc))
    print("\t\tFemale:  {} ({:.0f}%)".format(tot_f_conc,tot_f_conc/tot_conc*100))
    print("\t\tMale:    {} ({:.0f}%)".format(tot_m_conc,tot_m_conc/tot_conc*100))
    print("\t\tSex Ratio: {:.0f}".format(tot_m_conc/tot_f_conc if tot_f_conc>0 else "no females"))
    print("\t\tMaximum: {} ({} times)".format(np.amax(child_conc),np.count_nonzero(child_conc==np.amax(child_conc))))
    print("\t\tMinimum: {} ({} times)".format(np.amin(child_conc),np.count_nonzero(child_conc==np.amin(child_conc))))
    print("\tChild births: {} ({:.2f}% of conceptions)".format(tot_birth,tot_birth/tot_conc*100))
    print("\t\tFemale:  {} ({:.0f}%)".format(tot_f_birth,tot_f_birth/tot_birth*100))
    print("\t\tMale:    {} ({:.0f}%)".format(tot_m_birth,tot_m_birth/tot_birth*100))
    print("\t\tSex Ratio: {:.2f}".format(tot_m_birth/tot_f_birth if tot_f_birth>0 else "no females"))
    print("\t\tMaximum: {} ({} times)".format(np.amax(child_birth),np.count_nonzero(child_birth==np.amax(child_birth))))
    print("\t\tMinimum: {} ({} times)".format(np.amin(child_birth),np.count_nonzero(child_birth==np.amin(child_birth))))
    print("\tChildren reaching adulthood: {} ({:.0f}% of births, {:.0f}% of conceptions)".format(tot_surv,tot_surv/tot_birth*100,tot_surv/tot_conc*100))
    print("\t\tFemale:  {} ({:.2f}%)".format(tot_f_surv,tot_f_surv/tot_surv*100))
    print("\t\tMale:    {} ({:.2f}%)".format(tot_m_surv,tot_m_surv/tot_surv*100))
    print("\t\tSex Ratio: {:.2f}".format(tot_m_surv/tot_f_surv if tot_f_surv>0 else "no females"))
    print("\t\tMaximum: {} ({} times)".format(np.amax(child_surv),np.count_nonzero(child_surv==np.amax(child_surv))))
    print("\t\tMinimum: {} ({} times)".format(np.amin(child_surv),np.count_nonzero(child_surv==np.amin(child_surv))))
    print("\tMothers that died from birth: {}/{} ({:.0f}%)".format(num-tot_natural,num,(1-tot_natural/num)*100))
    print("\tAverage lifespan: {:.2f}".format(np.mean(np.asarray(death_ages).flatten())))
    
    if plots:
        plt.subplots(1,3)
        plt.tight_layout()
        plt.subplot(131)
        plt.hist(child_conc, np.arange(np.amax(child_conc)+2),align="left",color="gray",density=True)
        plt.axvline(np.mean(child_conc),0,1,color="k")
        plt.xlabel("# of conceptions")
        plt.ylabel("relative frequency")
        plt.subplot(132)
        plt.hist(child_birth, np.arange(np.amax(child_birth)+2),align="left",color="gray",density=True)
        plt.axvline(np.mean(child_birth),0,1,color="k")
        plt.xlabel("# of births")
        plt.ylabel("relative frequency")
        plt.subplot(133)
        plt.hist(child_surv, np.arange(np.amax(child_surv)+2),align="left",color="gray",density=True)
        plt.axvline(np.mean(child_surv),0,1,color="k")
        plt.xlabel("# of survivors")
        plt.ylabel("relative frequency")
        
        plt.subplots(1,3)
        plt.tight_layout()
        plt.subplot(131)
        m = max([np.amax(female_conc),np.amax(male_conc)])
        plt.hist(female_conc, np.arange(m+2),align="left", color="r", alpha=0.4,density=True,label="female")
        plt.hist(male_conc, np.arange(m+2),align="left", color="b", alpha=0.4,density=True,label="male")
        plt.axvline(np.mean(female_conc),0,1,color="r")
        plt.axvline(np.mean(male_conc),0,1,color="b")
        plt.legend()
        plt.xlabel("# of conceptions")
        plt.ylabel("relative frequency")
        plt.subplot(132)
        m = max([np.amax(female_birth),np.amax(male_birth)])
        plt.hist(female_birth, np.arange(m+2),align="left", color="r", alpha=0.4,density=True,label="female")
        plt.hist(male_birth, np.arange(m+2),align="left", color="b", alpha=0.4,density=True,label="male")
        plt.axvline(np.mean(female_birth),0,1,color="r")
        plt.axvline(np.mean(male_birth),0,1,color="b")
        plt.legend()
        plt.xlabel("# of births")
        plt.ylabel("relative frequency")
        plt.subplot(133)
        m = max([np.amax(female_surv),np.amax(male_surv)])
        plt.hist(female_surv, np.arange(m+2),align="left", color="r", alpha=0.4,density=True,label="female")
        plt.hist(male_surv, np.arange(m+2),align="left", color="b", alpha=0.4,density=True,label="male")
        plt.axvline(np.mean(female_surv),0,1,color="r")
        plt.axvline(np.mean(male_surv),0,1,color="b")
        plt.legend()
        plt.xlabel("# of survivors")
        plt.ylabel("relative frequency")
        
        female_conc = np.asarray(female_conc)
        male_conc = np.asarray(male_conc)
        conc_present = np.where(female_conc+male_conc>0)
        conc_diff = (female_conc-male_conc)[conc_present]/(female_conc+male_conc)[conc_present]
        female_birth = np.asarray(female_birth)
        male_birth = np.asarray(male_birth)
        birth_present = np.where(female_birth+male_birth>0)
        birth_diff = (female_birth-male_birth)[birth_present]/(female_birth+male_birth)[birth_present]
        female_surv = np.asarray(female_surv)
        male_surv = np.asarray(male_surv)
        surv_present = np.where(female_surv+male_surv>0)
        surv_diff = (female_surv-male_surv)[surv_present]/(female_surv+male_surv)[surv_present]
        
        plt.subplots(1,3)
        plt.tight_layout()
        plt.subplot(131)
        plt.hist(conc_diff,np.linspace(-1.1,1.1,12),color="gray",density=True)
        plt.axvline(np.mean(conc_diff),0,1,color="k")
        plt.grid()
        plt.xlabel("relative sex difference of conceptions (1=only female, -1=only male)")
        plt.ylabel("relative frequency")
        plt.subplot(132)
        plt.hist(birth_diff,np.linspace(-1.1,1.1,12),color="gray",density=True)
        plt.axvline(np.mean(birth_diff),0,1,color="k")
        plt.grid()
        plt.xlabel("relative sex difference of births (1=only female, -1=only male)")
        plt.ylabel("relative frequency")
        plt.subplot(133)
        plt.hist(surv_diff,np.linspace(-1.1,1.1,12),color="gray",density=True)
        plt.axvline(np.mean(surv_diff),0,1,color="k")
        plt.grid()
        plt.xlabel("relative sex difference of survivors (1=only female, -1=only male)")
        plt.ylabel("relative frequency")
        
        plt.figure()
        plt.hist(mother_deaths,np.arange(np.amax(mother_deaths)+2),color="r",alpha=0.4,density=True,align="left",label="mother deaths")
        plt.axvline(np.mean(mother_deaths),0,1,color="r",label="mother mean")
        plt.hist(death_ages,np.arange(np.amax(death_ages)+2),color="gray",density=True,align="left",label="children deaths")
        plt.axvline(np.mean(death_ages),0,1,color="k",label="children mean")
        plt.legend()
        plt.xlabel("death ages")
        plt.ylabel("relative frequency")
    plt.show()