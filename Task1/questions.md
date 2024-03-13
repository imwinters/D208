1. What is a real world application for a creating parallel slopes model, is the slope just the slope of the overall model applied to a different intercept? Why would we use that?

__This code produced the following logs__:

    
    mdl_price_vs_both_inter =  ols(
            "price_twd_msq ~ n_convenience + house_age_years + n_convenience:house_age_years",
            data=taiwan_real_estate
            ).fit()

    print(mdl_price_vs_both_inter.params)

    LOGS:

    mdl_readable_inter coefficients: 
        house_age_years[0 to 15]                   9.242
        house_age_years[15 to 30]                  6.872
        house_age_years[30 to 45]                  8.113
        house_age_years[0 to 15]:n_convenience     0.834
        house_age_years[15 to 30]:n_convenience    0.852
        house_age_years[30 to 45]:n_convenience    0.669
        dtype: float64


2. In the above logs why is house_age_years[XXX]:n_convenience the slope and house_age_years[XXX] the y intercept? How are these values calculated? The code is easy, but I want to make sure I understand what the return values are saying. How do I interpret this as I add more dimensions to a model?