def deriv(y, t, N, beta, gamma):
    S, I, R = y
    dSdt = -beta * S * I / N
    dIdt = beta * S * I / N - gamma * I
    dRdt = gamma * I
    return dSdt, dIdt, dRdt

# Standard SIR model
def SIR(beta, gamma):
    
    # Number of students, N.
    N = 1000
    
    # Initial number of students who have seen the video (I0) and number who have seen it and recovered (R0)
    I = 1
    R = 0
    
    # Everyone else, S0, is susceptible to getting the song stuck in their head.
    S = N - I - R
    # Initial conditions vector
    y0 = S, I, R

    # Contact rate, beta, and mean recovery rate, gamma, (in 1/days).
    beta = beta *(0.1)
    gamma = 1/gamma 
    
    # A grid of time points (in hours)
    t = np.linspace(0, 160, 160)

    # Integrate the SIR equations over the time grid, t.
    ret = odeint(deriv, y0, t, args=(N, beta, gamma))
    S, I, R = ret.T
    
    return (S, I, R)

def plot(S, I, R):
    t = np.linspace(0, 160, 160)
    # Plot the data on three separate curves for S(t), I(t) and R(t)
    fig = plt.figure(facecolor='w')
    ax = fig.add_subplot(111, facecolor='#dddddd', axisbelow=True)
    ax.plot(t, S, 'b', alpha=0.5, lw=2, label='Never seen the video')
    ax.plot(t, I, 'r', alpha=0.5, lw=2, label='Obsessed')
    ax.plot(t, R, 'g', alpha=0.5, lw=2, label='Over it')
    ax.set_xlabel('Time /hours')
    ax.set_ylabel('Number')
    ax.set_ylim(0,1200)
    ax.yaxis.set_tick_params(length=0)
    ax.xaxis.set_tick_params(length=0)
    ax.grid(b=True, which='major', c='w', lw=2, ls='-')
    legend = ax.legend()
    legend.get_frame().set_alpha(0.5)
    for spine in ('top', 'right', 'bottom', 'left'):
        ax.spines[spine].set_visible(False)
    plt.show()
    