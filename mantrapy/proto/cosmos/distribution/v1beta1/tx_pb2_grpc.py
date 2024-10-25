# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc
from cosmos.distribution.v1beta1 import tx_pb2 as cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2


class MsgStub:
    """Msg defines the distribution Msg service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.SetWithdrawAddress = channel.unary_unary(
            '/cosmos.distribution.v1beta1.Msg/SetWithdrawAddress',
            request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgSetWithdrawAddress.SerializeToString,
            response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgSetWithdrawAddressResponse.FromString,
        )
        self.WithdrawDelegatorReward = channel.unary_unary(
            '/cosmos.distribution.v1beta1.Msg/WithdrawDelegatorReward',
            request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgWithdrawDelegatorReward.SerializeToString,
            response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgWithdrawDelegatorRewardResponse.FromString,
        )
        self.WithdrawValidatorCommission = channel.unary_unary(
            '/cosmos.distribution.v1beta1.Msg/WithdrawValidatorCommission',
            request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgWithdrawValidatorCommission.SerializeToString,
            response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgWithdrawValidatorCommissionResponse.FromString,
        )
        self.FundCommunityPool = channel.unary_unary(
            '/cosmos.distribution.v1beta1.Msg/FundCommunityPool',
            request_serializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgFundCommunityPool.SerializeToString,
            response_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgFundCommunityPoolResponse.FromString,
        )


class MsgServicer:
    """Msg defines the distribution Msg service.
    """

    def SetWithdrawAddress(self, request, context):
        """SetWithdrawAddress defines a method to change the withdraw address
        for a delegator (or validator self-delegation).
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WithdrawDelegatorReward(self, request, context):
        """WithdrawDelegatorReward defines a method to withdraw rewards of delegator
        from a single validator.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def WithdrawValidatorCommission(self, request, context):
        """WithdrawValidatorCommission defines a method to withdraw the
        full commission to the validator address.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FundCommunityPool(self, request, context):
        """FundCommunityPool defines a method to allow an account to directly
        fund the community pool.
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MsgServicer_to_server(servicer, server):
    rpc_method_handlers = {
        'SetWithdrawAddress':
        grpc.unary_unary_rpc_method_handler(
            servicer.SetWithdrawAddress,
            request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgSetWithdrawAddress.FromString,
            response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgSetWithdrawAddressResponse.SerializeToString,
        ),
        'WithdrawDelegatorReward':
        grpc.unary_unary_rpc_method_handler(
            servicer.WithdrawDelegatorReward,
            request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgWithdrawDelegatorReward.FromString,
            response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgWithdrawDelegatorRewardResponse.SerializeToString,
        ),
        'WithdrawValidatorCommission':
        grpc.unary_unary_rpc_method_handler(
            servicer.WithdrawValidatorCommission,
            request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgWithdrawValidatorCommission.FromString,
            response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgWithdrawValidatorCommissionResponse.SerializeToString,
        ),
        'FundCommunityPool':
        grpc.unary_unary_rpc_method_handler(
            servicer.FundCommunityPool,
            request_deserializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgFundCommunityPool.FromString,
            response_serializer=cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2
            .MsgFundCommunityPoolResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        'cosmos.distribution.v1beta1.Msg',
        rpc_method_handlers,
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class Msg:
    """Msg defines the distribution Msg service.
    """

    @staticmethod
    def SetWithdrawAddress(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cosmos.distribution.v1beta1.Msg/SetWithdrawAddress',
            cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgSetWithdrawAddress.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgSetWithdrawAddressResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def WithdrawDelegatorReward(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cosmos.distribution.v1beta1.Msg/WithdrawDelegatorReward',
            cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgWithdrawDelegatorReward.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgWithdrawDelegatorRewardResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def WithdrawValidatorCommission(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cosmos.distribution.v1beta1.Msg/WithdrawValidatorCommission',
            cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgWithdrawValidatorCommission.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgWithdrawValidatorCommissionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def FundCommunityPool(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            '/cosmos.distribution.v1beta1.Msg/FundCommunityPool',
            cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgFundCommunityPool.SerializeToString,
            cosmos_dot_distribution_dot_v1beta1_dot_tx__pb2.
            MsgFundCommunityPoolResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
