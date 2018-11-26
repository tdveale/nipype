# AUTO-GENERATED by tools/checkspecs.py - DO NOT EDIT
from __future__ import unicode_literals
from ..preprocess import RealignUnwarp


def test_RealignUnwarp_inputs():
    input_map = dict(
        est_basis_func=dict(field='uweoptions.basfcn', ),
        est_first_order_effects=dict(field='uweoptions.fot', ),
        est_jacobian_deformations=dict(field='uweoptions.jm', ),
        est_num_of_iterations=dict(
            field='uweoptions.noi',
            maxlen=1,
            minlen=1,
            usedefault=True,
        ),
        est_re_est_mov_par=dict(field='uweoptions.rem', ),
        est_reg_factor=dict(
            field='uweoptions.lambda',
            maxlen=1,
            minlen=1,
            usedefault=True,
        ),
        est_reg_order=dict(field='uweoptions.regorder', ),
        est_second_order_effects=dict(field='uweoptions.sot', ),
        est_taylor_expansion_point=dict(
            field='uweoptions.expround',
            usedefault=True,
        ),
        est_unwarp_fwhm=dict(field='uweoptions.uwfwhm', ),
        fwhm=dict(field='eoptions.fwhm', ),
        in_files=dict(
            copyfile=True,
            field='data.scans',
            mandatory=True,
        ),
        interp=dict(field='eoptions.einterp', ),
        matlab_cmd=dict(),
        mfile=dict(usedefault=True, ),
        out_prefix=dict(
            field='uwroptions.prefix',
            usedefault=True,
        ),
        paths=dict(),
        phase_map=dict(
            copyfile=False,
            field='data.pmscan',
        ),
        quality=dict(field='eoptions.quality', ),
        register_to_mean=dict(field='eoptions.rtm', ),
        reslice_interp=dict(field='uwroptions.rinterp', ),
        reslice_mask=dict(field='uwroptions.mask', ),
        reslice_which=dict(
            field='uwroptions.uwwhich',
            maxlen=2,
            minlen=2,
            usedefault=True,
        ),
        reslice_wrap=dict(field='uwroptions.wrap', ),
        separation=dict(field='eoptions.sep', ),
        use_mcr=dict(),
        use_v8struct=dict(
            min_ver='8',
            usedefault=True,
        ),
        weight_img=dict(field='eoptions.weight', ),
        wrap=dict(field='eoptions.ewrap', ),
    )
    inputs = RealignUnwarp.input_spec()

    for key, metadata in list(input_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(inputs.traits()[key], metakey) == value
def test_RealignUnwarp_outputs():
    output_map = dict(
        mean_image=dict(),
        modified_in_files=dict(),
        realigned_unwarped_files=dict(),
        realignment_parameters=dict(),
    )
    outputs = RealignUnwarp.output_spec()

    for key, metadata in list(output_map.items()):
        for metakey, value in list(metadata.items()):
            assert getattr(outputs.traits()[key], metakey) == value
