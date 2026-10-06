from Signature_portfolios_optimize_realdata_PCA import learn_sig_weights_REALDATA_TCgradient

learn_sig_weights_REALDATA_TCgradient(
    data_name="ATX",
    order_sig=2,
    ranks=list(range(1, 21)),
    t_insample=3000,
    t_outsample=750,
    bounds=5,
    prop_cost=0.01,      # 1% proportional transaction costs
    rank_based=True,
    randomsig=False,
    objective="MV",
    risk_factor=1,
    pca_dim=50,
    n_jobs=4,
    end_time=50,
    t_start=0,
)




